#!/bin/bash

# Function to start Flask
start_flask() {
    echo "Starting Flask..."
    flask run --host=0.0.0.0 --port=5000 &
    FLASK_PID=$!  # Store the process ID for later stopping
    echo "Flask started with PID $FLASK_PID"
}

# Function to start JupyterLab
start_jupyter() {
    echo "Starting JupyterLab..."
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root &
    JUPYTER_PID=$!  # Store the process ID for later stopping
    echo "JupyterLab started with PID $JUPYTER_PID"
}

# Parse command line arguments
if [[ "$1" == "flask" ]]; then
    start_flask
elif [[ "$1" == "jupyter" ]]; then
    start_jupyter
elif [[ "$1" == "both" ]]; then
    start_flask
    start_jupyter
else
    echo "Usage: ./start_services.sh [flask|jupyter|both]"
fi