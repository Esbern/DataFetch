#!/bin/bash

# Function to stop Flask
stop_flask() {
    echo "Stopping Flask..."
    pkill -f "flask run"
    echo "Flask stopped"
}

# Function to stop JupyterLab
stop_jupyter() {
    echo "Stopping JupyterLab..."
    pkill -f "jupyter lab"
    echo "JupyterLab stopped"
}

# Parse command line arguments
if [[ "$1" == "flask" ]]; then
    stop_flask
elif [[ "$1" == "jupyter" ]]; then
    stop_jupyter
elif [[ "$1" == "both" ]]; then
    stop_flask
    stop_jupyter
else
    echo "Usage: ./stop_services.sh [flask|jupyter|both]"
fi