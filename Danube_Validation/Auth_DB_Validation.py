import psycopg2
from source_and_destination_table import authDataBaseValidations
import os
from dotenv import load_dotenv

# Define your database connection parameters
def execute_query(query, connection):
    cur = connection.cursor()
    cur.execute(query)
    result = cur.fetchone()[0]
    cur.close()
    return result

def validate_tables(config1, config2):
    conn = None
    conn1 = None
    try:
        # Connect to the databases
        conn = psycopg2.connect(**config1)
        conn1 = psycopg2.connect(**config2)

        for validation in authDataBaseValidations:
            source_count = execute_query(validation["source_query"], conn1)
            dest_count = execute_query(validation["dest_query"], conn)

            print(f"Validation for {validation['source_table']} vs {validation['dest_table']}:")
            print(f"Source count: {source_count}")
            print(f"Destination count: {dest_count}\n")

        conn.close()
        conn1.close()

    except psycopg2.Error as e:
        print("Error executing SQL statement:", e)
    finally:
        # Close the connections if they are open
        if conn:
            conn.close()
        if conn1:
            conn1.close()

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    V1_config = {
        'dbname': os.getenv('dbname1'),
        'user': os.getenv('user1'),
        'password': os.getenv('password1'),
        'host': os.getenv('host1'),
        'port': os.getenv('port1')  # Fixed the key for port1
    }

    V2_config = {
        'dbname': os.getenv('dbname2'),
        'user': os.getenv('user2'),
        'password': os.getenv('password2'),
        'host': os.getenv('host2'),
        'port': os.getenv('port2')  # Fixed the key for port2
    }

    # Validate tables
    validate_tables(V1_config, V2_config)
