import os
import logging
from fetch_and_store import init

# Configure logging to see output during testing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_initialize():
    """
    Test to check if the initialize function is working correctly.
    - It should create the data folder if it doesn't exist.
    - It should correctly initialize the library.
    """
    
    # Run the initialize function (this will check if we're in Docker and set paths accordingly)
    conn = initialize()

    # Check if the appropriate data folder exists based on whether we're in Docker or outside
    if os.getenv("RUNNING_IN_DOCKER") == "true":
        data_folder = '/app/data'  # Inside Docker
    else:
        data_folder = os.getenv("DATA_FOLDER_EXTERNAL")  # Outside Docker
    
    # Check if the data folder was created
    assert os.path.exists(data_folder), f"Data folder does not exist: {data_folder}"
    logging.info(f"Data folder exists at: {data_folder}")

    # Optionally, check if the database connection (GeoPackage or Postgres) is valid
    assert conn is not None, "Failed to initialize database connection"
    logging.info("Database connection initialized successfully")

if __name__ == "__main__":
    test_initialize()