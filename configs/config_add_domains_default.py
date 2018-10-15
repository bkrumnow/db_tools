""" CONFIG FOR S&P2019 Paper
"""
import os

# Paths and file names
DIRECTORY_PATH = "/any/"
OUTPUT_FILE = "database_x.sqlite"

OUTPUT_DATABASE = os.path.join(DIRECTORY_PATH, OUTPUT_FILE)

TABLE_CHANGES = [{"table_name":"table1", "column_name":"column1", "url_column_name":"URL", "counter":1}]