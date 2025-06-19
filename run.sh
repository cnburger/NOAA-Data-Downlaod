#!/bin/bash

# Make sure we exit on error
set -e

echo "Starting NOAA data download script..."

# Run the Python script
python3 ghcnd_station_csv_download.py

echo "Download complete. Files saved in the NOAA/ directory."
