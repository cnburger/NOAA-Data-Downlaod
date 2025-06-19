# NOAA Data Download

A **super simple** Python script to download daily climate data from NOAA's Global Historical Climatology Network (GHCN-D), using the public AWS S3 bucket.

## How to Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/NOAA-Data-Download.git
   cd NOAA-Data-Download
   ```

2. **Install dependencies**:
   Make sure you have Python 3 installed, then install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Edit the station list**:
   Open the `ghcnd_station_csv_download.py` file and modify the `STATION_LIST` variable:

   ```python
   STATION_LIST = ['KE000063740', 'USW00094728']  # Example stations
   ```

4. **Run the script**:

   ```bash
   python3 ghcnd_station_csv_download.py
   ```

5. **Find your data**:
   The downloaded CSV files will be saved in the `NOAA_CSV/` directory.

## Notes

* You can find a list of all NOAA station IDs in the metadata file:
  [ghcnd-stations.txt](http://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt)

* Data is hosted publicly in NOAA's AWS S3 bucket:
  [NOAA GHCN on AWS](https://registry.opendata.aws/noaa-ghcn/)

## Acknowledgments

This project was inspired by the GHCN-D documentation from the NOAA Big Data Program:
[NOAA Big Data Docs – GHCN-D](https://github.com/NOAA-Big-Data-Program/nodd-data-docs/tree/main/GHCN-D)
