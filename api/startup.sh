#!/bin/bash

# Check if required environment variables are set
REQUIRED_VARS=("PGPASSWORD" "PGHOST" "PGDATABASE" "PGUSER")

for var in "${REQUIRED_VARS[@]}"; do
    if [ -z "${!var}" ]; then
        echo "Error: Environment variable $var is not set."
        echo "Please set the $var variable before proceeding."
        exit 1
    fi
done

# Inform the user about the database connection details
echo "Database connection details are as follows:"

# Print values of environment variables except for PGPASSWORD
echo "PGHOST: $PGHOST"
echo "PGDATABASE: $PGDATABASE"
echo "PGUSER: $PGUSER"

# Run the Python application
python3 app.py