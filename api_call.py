import requests
import argparse
import logging
import threading
import requests
from datetime import datetime

#global conffiguration
API_URL="https://ifconfig.co"

# Configure the logging
logging.basicConfig(level=logging.DEBUG, filename='api_calls.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

#calling the api & logs the result
def call_api():
    try:
        res = requests.get(API_URL, timeout=1)
        if res.status_code == 200:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"Successfully called API at {API_URL} at {current_time}")  
    except requests.exceptions.RequestException as err:
        logging.error(f"Failed to call API at {API_URL}. Error: {err}")

#schedule api calls based on the provided time stamps, multiple same time slots execute parallely
def schedule_calls(timestamps):
    # Remove duplicate timestamps and sort them
    unique_timestamps = sorted(set(timestamps))

    for tstamp in unique_timestamps:
        # Get the current time in HH:MM:SS format & converting a datetime object
        now_time = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")

        # Convert the given timestamp string to a datetime object
        tstamp_time = datetime.strptime(tstamp, "%H:%M:%S")

        # Calculate the delay in seconds before the API call should be made
        delay = (tstamp_time - now_time).total_seconds()

        if delay > 0:
            # Schedule API call after delay seconds
            threading.Timer(delay, call_api).start()
        else:
            # Log an error if the timestamp is in the past
            logging.error(f"{tstamp} is in the past")
            

def main():
    parser = argparse.ArgumentParser(description="Program.")
    parser.add_argument("timestamps", type=str, nargs="?", default="", help="Comma-separated timestamps (e.g., '12:30:00,13:00:00')")
    args = parser.parse_args()

    if not args.timestamps:
        print("Error: Please provide timestamps as a comma-separated list (e.g., '12:30:00,13:00:00')")
        return

    timestamps = args.timestamps.split(",")
    schedule_calls(timestamps)

if __name__ == "__main__":
    main()

            

            
            
            

            
        
    
    
    
    

