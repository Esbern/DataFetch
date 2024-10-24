
# Set working directory
WORKDIR /workspace

# Install necessary libraries and build tools for GeoPackage, Fiona, and GDAL
RUN apt-get update && apt-get install -y \
    build-essential \
    sqlite3 \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    && rm -rf /var/lib/apt/lists/*

# Set GDAL version environment variable to match the installed version
ENV GDAL_VERSION=3.3.2
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install Python packages
RUN pip install --no-cache-dir \
    requests \
    fiona==1.10.1 \
    geopandas \
    python-dotenv

# Ensure a development-friendly environment by installing common tools
RUN pip install --no-cache-dir jupyterlab

# Update package list again and install curl and git, then install VS Code Remote Development
RUN apt-get update && apt-get install -y curl git \
    && curl -fsSL https://code-server.dev/install.sh | sh

# Expose port 8080 for JupyterLab
EXPOSE 8080

# Command to keep the container running (used for dev purposes)
CMD ["tail", "-f", "/dev/null"]