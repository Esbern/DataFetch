import logging
import os
import sqlite3
import psycopg2
from dotenv import load_dotenv

def connect_to_geopackage(gpkg_path):
    """
    Connects to a GeoPackage database.
    
    :param gpkg_path: Path to the GeoPackage file.
    :return: SQLite connection object.
    """
    conn = sqlite3.connect(gpkg_path)
    return conn


def create_metadata_table(conn):
    """
    Ensures the metadata table exists in the database.
    
    :param conn: Database connection object.
    """
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS metadata (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        value TEXT
    )
    """)
    conn.commit()
    

# Configure logging
logging.basicConfig(level=logging.INFO)

def initialize():
    """
    Initializes the library by:
    - Loading environment variables from the .env file.
    - Checking whether it's running inside a Docker container.
    - Selecting the appropriate data folder.
    - Connecting to the specified database (GeoPackage or PostgreSQL).
    - Ensuring the metadata table exists.
    """
    
    # Load environment variables from the .env file
    load_dotenv()

    # Configure logging level from .env
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level_str, logging.INFO)  # Default to INFO if invalid
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.info(f"Logging level set to {log_level_str}")

    # Check if running inside Docker by looking for RUNNING_IN_DOCKER environment variable
    if os.getenv("RUNNING_IN_DOCKER") == "true":
        data_folder = '/data'  # Hardcoded path inside Docker container
        logging.info("Running inside Docker, using internal data folder")
    else:
        data_folder = os.getenv("DATA_FOLDER_EXTERNAL")  # Path from .env for external use
        logging.info(f"Running outside Docker, using external data folder: {data_folder}")

    # Ensure the data folder exists
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        logging.info(f"Data folder created at {data_folder}")
    else:
        logging.info(f"Data folder already exists at {data_folder}")
    
    # Check the database type and connect accordingly
    db_type = os.getenv("DB_TYPE")
    
    if db_type == "geopackage":
        gpkg_path = os.path.join(data_folder, "metadata.gpkg")
        if not os.path.exists(gpkg_path):
            open(gpkg_path, 'w').close()
            logging.info(f"GeoPackage database created at {gpkg_path}")
        conn = connect_to_geopackage(gpkg_path)
    elif db_type == "postgres":
        conn = connect_to_postgres()
    else:
        raise ValueError("DB_TYPE in .env must be either 'geopackage' or 'postgres'")
    
    # Ensure the metadata table exists
    if conn:
        create_metadata_table(conn)
    

    logging.info("Initialization complete.")
    return conn