""" Runs all sql queries, that can be found in a directory
"""
import csv
import sqlite3
import sys
import os
import glob
import tldextract as tld

from configs.config_db_merge import OUTPUT_DATABASE
TABLE_CHANGES = [{"table_name":"Scripts", "column_name":"domain_name", "url_column_name":"URL", "counter":3}]
    
def modify_dataset():
    """ Executes and prints all queries
    """
    con = database_connect(OUTPUT_DATABASE)
    alter_table(con, TABLE_CHANGES)
    update_table(con, TABLE_CHANGES)
    con.close()

def alter_table(con, changes):
    alter_script = "ALTER TABLE {0}{2} ADD COLUMN {1} TEXT;"
    try:
        cursor = con.cursor()
        for change in changes:
            for i in range(1,change['counter']+1):
                cursor.execute(alter_script.format(change["table_name"],change["column_name"], i))
        con.commit()
    except sqlite3.Error as e:
        print("ERROR: {}".format(e))
        print("File was {}".format(file_database))
        con.close()

def database_connect(file_database):
    con = None
    try:
        con = sqlite3.connect(file_database)
        return con
    except sqlite3.Error as e:
        print("ERROR: {}".format(e))
        print("File was {}".format(file_database))
        if con:
            con.close()
    
def update_table(con, changes):
    """Merges the table credentials of the given database with the local database."""
    select_query = "SELECT {1} FROM {0}{2}"
    update_query = "UPDATE {0}{5} SET {1}=\"{2}\" WHERE {3}=\"{4}\""
    cursor_select = con.cursor()
    cursor_update = con.cursor()
    try:
        for change in changes:
            for i in range(1,change['counter']+1):
                for row in cursor_select.execute(select_query.format(change["table_name"], change["url_column_name"], i)):
                    url = row[0]
                    domain = receivce_domain_name(url)
                    print(url)
                    cursor_update.execute(update_query.format(change["table_name"], change["column_name"], domain, change["url_column_name"], url, i))
        con.commit()
    except sqlite3.Error as e:
        print("ERROR: {}".format(e))
        con.close()        

def receivce_domain_name(url):
    extract = tld.extract(url)
    domain = ".".join(extract)
    if extract.subdomain == "":
        domain = domain[1:]
    return domain if domain != "" else None


if __name__ == '__main__':
    modify_dataset()