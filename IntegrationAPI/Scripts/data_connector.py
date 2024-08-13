
# data_connector.py

import logging
import sqlite3

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/IntegrationAPI/Logs/integration_errors.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_database(db_path):
    """
    Establishes a connection to the specified SQLite database.
    Args:
        db_path (str): The path to the SQLite database file.
    Returns:
        sqlite3.Connection: The database connection object, or None if an error occurs.
    """
    try:
        conn = sqlite3.connect(db_path)
        logging.info(f"Connected to database at {db_path}.")
        print(f"Connected to database at {db_path}.")
        return conn

    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        print(f"Error: {e}")
        return None

def execute_query(conn, query):
    """
    Executes a SQL query on the connected database.
    Args:
        conn (sqlite3.Connection): The database connection object.
        query (str): The SQL query to execute.
    Returns:
        list: The result of the query, or None if an error occurs.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info("Query executed successfully.")
        print("Query executed successfully.")
        return result

    except sqlite3.Error as e:
        logging.error(f"Error executing query: {e}")
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    db_connection = connect_to_database('/mnt/data/TIGTA_Automation_Suite/IntegrationAPI/Data/example.db')
    if db_connection:
        query_result = execute_query(db_connection, "SELECT * FROM example_table;")
        print(query_result)
