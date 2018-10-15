# Description #
A small bunch of tools to execute common database operations.
Just edit the config with the certain file paths or queries in order to start

# Installation #
It is recommended to use tools to manage the version of python libraries, such as virtualenv

	python -m pip install -r requirements.txt

# Tools #
* db_merge: Creates a new database with all given databases (which contain the same column names)
* run_queries: Takes all *.sql files from a server and executes the containing sql queries for a given database
* add_domain_names: Alters tables and appends a new column with domains which can be derived from a column with urls
