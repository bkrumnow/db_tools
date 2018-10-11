import os

# Paths and file names
DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
SUB_DIRECTORY = "/any/"
OUTPUT_FILE = "database_x.sqlite"
PATH = os.path.join(DIRECTORY_PATH, SUB_DIRECTORY)

OUTPUT_DATABASE = os.path.join(PATH, OUTPUT_FILE)

SOURCE_DATABASES = [
    "thserver/crawl-data.sqlite"
    ,"benserver/crawl-data.sqlite"
    ,"benserver/crawl-data_previous_cleaned.sqlite"
]

# SQL statements
CREATE_STATEMENTS = [
    "CREATE TABLE example{0} ( task_id INTEGER PRIMARY KEY AUTOINCREMENT, start_time DATETIME DEFAULT CURRENT_TIMESTAMP, manager_params TEXT NOT NULL, openwpm_version TEXT NOT NULL, browser_version TEXT NOT NULL)"
]

INSERT_STATEMENTS = [
    {"select":"SELECT * FROM example;","insert":"INSERT INTO example{} VALUES (?, ?, ?, ?, ?);"}
]
    