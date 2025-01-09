import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import json
import logging
import csv
from datetime import datetime

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
                    , filemode='w')

#Get .env path
dotenv_path = join(dirname(__file__), '.env')
#load the .env file
load_dotenv(dotenv_path)

LATITUDE = os.getenv('LATITUDE')
LONGITUDE = os.getenv('LONGITUDE')
START_DATE = os.getenv('START_DATE')
END_DATE = os.getenv('END_DATE')
API_KEY = os.getenv('API_KEY')

url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={LATITUDE}&lon={LONGITUDE}&start={START_DATE}&end={END_DATE}&appid={API_KEY}"

try:
        logging.info('Fetching data. . .')
        response = requests.get(url)
        response.raise_for_status()
        air_quality_json = response.json()
        data = air_quality_json['list']
        air_quality_index = {
              1: 'Good',
              2: 'Fair',
              3: 'Moderate',
              4: 'Poor',
              5: 'Very Poor'        
              }
        
        with open('data.csv', 'w', newline='') as file:
            logging.info('Create csv file of Air Quality data. . .')
            writer = csv.writer(file)
            field = ['Date', 'Air Quality']
            writer.writerow(field)
            for i in data:
                date = datetime.fromtimestamp(i['dt'])
                air_quality = air_quality_index[i['main']['aqi']]
                writer.writerow([date, air_quality])


except json.JSONDecodeError as e:
    logging.error(e)
    print(e)
except requests.exceptions.HTTPError as e:
        error_details = ''
        if response.status_code == 401: 
            error_details = 'Invalid API KEY'
        elif response.status_code == 400: 
            error_details = f'Invalid Location - {e}'
        else:
             error_details = f'{response.status_code} - Unknown Error has Occured'
        print(error_details)
        logging.error(error_details)
