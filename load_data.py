import pandas as pd
import mysql.connector
from mysql.connector import Error

def load_data_to_mysql(csv_file, db_config):
    """
    Reads a CSV file and loads it into the MySQL database.
    
    Args:
        csv_file (str): Path to the CSV file.
        db_config (dict): Database configuration dictionary.
    """
    try:
        # 1. Read CSV Data
        print(f"Reading data from {csv_file}...")
        df = pd.read_csv(csv_file)
        
        # Handle NaN values (replace with None for MySQL NULL)
        # Convert to object type first to handle Nones in numeric columns
        df = df.astype(object)
        df = df.where(pd.notnull(df), None)
        
        # 2. Connect to Database
        print("Connecting to MySQL database...")
        connection = mysql.connector.connect(**db_config)
        
        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected successfully.")
            
            # 3. Insert Data
            # Prepare the INSERT statement
            # Assuming the CSV columns match the table columns in order
            # movie_id, title, genre, rating, budget_million, gross_million, director, lead_actor, release_year
            
            insert_query = """
            INSERT INTO movies (movie_id, title, genre, rating, budget_million, gross_million, director, lead_actor, release_year)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Convert DataFrame to list of tuples for executemany
            data_to_insert = [tuple(x) for x in df.to_numpy()]
            
            print(f"Inserting {len(data_to_insert)} rows...")
            cursor.executemany(insert_query, data_to_insert)
            
            connection.commit()
            print("Data loaded successfully!")
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    # Database Configuration
    # NOTE: Update 'user' and 'password' with your actual MySQL credentials
    db_config = {
        'host': 'localhost',
        'database': 'imdb_analysis',
        'user': 'root',      # Replace with your MySQL username
        'password': '12345678'       # Replace with your MySQL password
    }
    
    csv_file_path = 'imdb_movies.csv'
    
    load_data_to_mysql(csv_file_path, db_config)
