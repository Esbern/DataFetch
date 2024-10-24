# Use the official Python slim image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /workspace

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    sqlite3 \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages including Flask
RUN pip install --no-cache-dir \
    requests \
    fiona==1.10.1 \
    geopandas \
    python-dotenv \
    psycopg2-binary \
    flask \
    jupyterlab

# Expose ports
EXPOSE 5000  
EXPOSE 8888  

# Keep container running in idle mode
CMD ["tail", "-f", "/dev/null"]