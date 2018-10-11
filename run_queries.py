""" Runs all sql queries, that can be found in a directory
"""
import csv
import sqlite3
import sys
import os
import glob

from configs.config_querries import DATABASE
from configs.config_querries import SQL_DIRECTORY

def find_sqls(directory):
    os.chdir(directory)
    return glob.glob("*.sql")
    
def create_statistic():
    """ Executes and prints all queries
    """
    files = find_sqls(SQL_DIRECTORY)
    con = None
    con = database_connect(DATABASE)
    cur = con.cursor()
    for name in files:
        with open(os.path.join(SQL_DIRECTORY, name), "r") as f:
            script = f.read()
            print(script)
            execute_query(cur, name, script)
    if con:
        con.close()

def database_connect(file_database):
    con = None
    try:
        con = sqlite3.connect(file_database)
        return con
    except sqlite3.Error as e:
        print("ERROR: {}".format(e))
        print("File was {}".format(file_database))
    
def execute_query(cursor, name, script):
    """Merges the table credentials of the given database with the local database."""
    try:
        for row in cursor.execute(script):
            print("{} --> {}".format(name, row))
    except sqlite3.Error as e:
        print("ERROR: {}".format(e))
        
if __name__ == '__main__':
    create_statistic()