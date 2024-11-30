import pandas as pd
import requests


from config import Config
def fecth_air_quality(country_name,state_name,city_name,start_date,end_date):
    """
    fecth data pada kualitas udara pada Air visual api,
    parameter:
        country_name (str): 
        state_nane (str):
        city_name (str):
        start_date(str):
        end_date(str):
    returns:
    pd.Dateframe: the airu quality data as a Python dictionary
    save = True
    """
    url = (f"https://api.airvisual.com/v2/history?city={Config.country}&state={Config.state}&country={Config.country}"
           f"&start={Config.start_date}&end={Config.end_date}&key={Config.api_key}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        air_quality_json = response.json()
    except Exception as err:
        print(err)
    return air_quality_json
