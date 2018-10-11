""" Finds results, which belong to the Alexa Top 1M and copies them into a new database
"""
import csv
import sqlite3
import sys

from configs.config_creation import SOURCE_DATABASES
from configs.config_creation import DATABASE
from configs.config_creation import CREATE_STATEMENTS
from configs.config_creation import INSERT_STATEMENTS


def start():
    db_name = "database_x.sqlite"
    create_tables(OUTPUT_DATABASE, SOURCE_DATABASES)
    copy_entries(OUTPUT_DATABASE, SOURCE_DATABASES)
    
def database_connect(file_database):
    con = None
    try:
        con = sqlite3.connect(file_database)
        return con
    except sqlite3.Error as e:
        print("ERROR in CREATE: {}".format(e))
        print("File was {}".format(file_database))


def create_tables(new_db, old_dbs):
    """ Executes and prints all queries
    """
    con = database_connect(new_db)
    try:
        cursor = con.cursor()
        for i, database in enumerate(old_dbs, start=1):
            for s in CREATE_STATEMENTS:
                #print(s.format(i))
                cursor.execute(s.format(i))
    except:
        raise
    finally:
        if con:
            con.close()
        
        

def copy_entries(new_db, old_dbs):
    """ Merges the table credentials of the given database with the local database.
    """
    for i,database in enumerate(old_dbs, start=1):
        try:
            con = database_connect(new_db)
            cursor = con.cursor()
            
            con_src = database_connect(database)
            cursor_src = con_src.cursor()
        
            for query in INSERT_STATEMENTS:
                cursor_src.execute(query["select"])
                content = cursor_src.fetchall()
                for row in content:
                    print("{} --> {}".format(query["select"], row))
                    cursor.execute(query["insert"].format(i), row)
                con.commit()

        except sqlite3.Error as e:
            print("ERROR in INSERT: {}".format(e))
        finally:
            if con:
                con.close()
            if con_src:
                con_src.close()

if __name__ == '__main__':
    start()