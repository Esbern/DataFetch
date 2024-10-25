"""
FetchAndStore

A Python library for fetching data from public Danish APIs and storing it locally 
with associated metadata in a GeoPackage. The library provides simple APIs for fetching 
data (e.g., addresses) and keeping track of when and how the data was retrieved.

Modules:
    fetch_data: Contains functions to fetch data from APIs.
    metadata: Handles storing and managing metadata in a GeoPackage.

Usage:
    from fetch_and_store import fetch_addresses, connect_to_geopackage
    
    # Fetch data
    fetch_addresses("101", "addresses.csv")
    
    # Work with metadata
    conn = connect_to_geopackage("metadata.gpkg")
    create_metadata_table(conn)
    insert_metadata(conn, "address", "addresses.csv", "/data/addresses.csv")
"""
from .initialize import initialize  # Import initialize function from the initialize.py file