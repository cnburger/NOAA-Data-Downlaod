import pandas as pd
import os

'''
This script can download daily climate data from NOAA's Global Historical Climatology Network (GHCN-D).
It reads .csv files directly from the NOAA S3 bucket and saves them locally.

As of this writing, NOAA hosts data from over 150,000 weather stations worldwide. The list of station
IDs can be found in the 'ghcnd-stations.txt' metadata file, available here:
https://registry.opendata.aws/noaa-ghcn/ or directly at:
http://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt
'''

# Directory where NOAA station CSVs are hosted
NOAA_DIR = 'https://noaa-ghcn-pds.s3.amazonaws.com/csv/by_station/'

# Example list of station IDs (can be expanded or read from metadata)
STATION_LIST = ['KE000063740']  # JOMO KENYATTA INTL

# Ensure output directory exists
output_dir = 'NOAA_CSV'
os.makedirs(output_dir, exist_ok=True)

for station in STATION_LIST:
    url = f"{NOAA_DIR}{station}.csv"
    df = pd.read_csv(url)
    df.to_csv(os.path.join(output_dir, f"{station}.csv"), index=False)
    print(f"Downloaded and saved data for station: {station}")


"""
This script was inspired by the NOAA Big Data Program.
More information and documentation is available at:
https://github.com/NOAA-Big-Data-Program/nodd-data-docs/tree/main/GHCN-D
"""
