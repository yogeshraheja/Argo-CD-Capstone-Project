#!/bin/bash

# Check if required environment variables are set
REQUIRED_VARS=("API_HOST" "API_PORT")

for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        echo "Error: Environment variable $var is not set."
        echo "Please set the $var variable before proceeding."
        exit 1
    fi
done

# Inform the user about the database connection details
echo "API application connection details are as follows:"

# Print values of environment variables except for PGPASSWORD
echo "API_HOST: $API_HOST"
echo "API_PORT: $API_PORT"

# Run the Python application
python3 app.py