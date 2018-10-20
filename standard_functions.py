""" Programm for the shepherd project to add the alexa position into the result dataset
"""
import csv
import sqlite3
import sys

def database_connect(file_database):
    con = None
    try:
        con = sqlite3.connect(file_database)
        return con
    except sqlite3.Error as e:
        print("ERROR in CREATE: {}".format(e))
        print("File was {}".format(file_database))


def add_table(con, queries):
    """ Executes and prints all queries
    """
    cursor = con.cursor()
    try:
        for query in queries:
            cursor.execute(query)
        con.commit()        
    except:
        raise
        if con:
            con.close()
        
        
