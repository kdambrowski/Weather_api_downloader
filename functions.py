import json
import os
from datetime import datetime
import warnings

import pandas as pd
import requests

from setings import KEY, features_list


def create_city_list_file(filename, cities):
    """
    Create a text file containing a list of cities.

    Args:
        filename (str): The name of the output text file.
        cities (list): A list of cities to be written to the file.

    Returns:
        str: The filename of the created text file.
    """
    if not filename.endswith(".txt"):
        filename += ".txt"
    with open(filename, 'w') as file:
        for city in cities:
            file.write(city + '\n')
    print(f'File {filename} with cities has benn created successfully ')
    return filename

def print_city_from_config_file(config_file_name):
    """
    Print information about cities from a configuration file.

    Args:
        config_file_name (str): The name of the configuration file.

    Returns:
        None
    """
    for city in config_file_opener(config_file_name):
        print(format(f'Information about the weather will be displayed for the city: {city}', '_^80'))


def config_file_opener(config_file_name):
    """
    Open and read a configuration file containing a list of cities.

    Args:
        config_file_name (str): The name of the configuration file.

    Returns:
        list: A list of cities read from the file.
    """
    with open(config_file_name, 'r') as f:
        line_data = [line.strip() for line in f]
        return line_data


def get_weather_data(city, current_or_forecast= 'forecast'):
    """
    Retrieve weather data for a given city from an external API.

    Args:
        city (str): The name of the city.
        current_or_forecast (str): 'current' to retrieve current weather data, 'forecast' to retrieve forecast data.

    Returns:
        dict: Weather data for the specified city and time.
    """
    url = f'http://api.weatherapi.com/v1/{current_or_forecast}.json?key={KEY}&q={city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Data for city {city} does not exist or has been server connection interruption')
        return None


def display_weather_info(city, weather_data, current_or_forecast= 'current'):
    """
    Display weather information for a given city.

    Args:
        city (str): The name of the city.
        weather_data (dict): Weather data for the city.
        current_or_forecast (str): 'current' for current weather data, 'forecast' for forecast data.

    Returns:
        None
    """
    try:
        if weather_data:
            print(f'Weather for {city}:')
            print(f'Local date and time for data extraction: {weather_data[current_or_forecast]["last_updated"]}')
            print(f'Temperature: {weather_data[current_or_forecast]["temp_c"]}°C')
            print(f'Wind: {weather_data[current_or_forecast]["wind_kph"]} km/h')
            print(f'Pressure: {weather_data[current_or_forecast]["pressure_mb"]} hPa')
            print(f'Weather condition: {weather_data[current_or_forecast]["condition"]["text"]}')
            print('---')
        else:
            print(f'No weather data available for {city}')
    except KeyError as e:
        print(f'Error: Missing key in weather data for {city}: {e}')
    except Exception as e:
        print(f'An error occurred while displaying weather info for {city}: {str(e)}')


def create_directory_structure(year, month, day, city, dir_path= ""):
    """
    Create a directory structure for storing weather data.

    Args:
        year (int): The year for the directory structure.
        month (int): The month for the directory structure.
        day (int): The day for the directory structure.
        city (str): The name of the city.
        dir_path (str): The base directory path (optional).

    Returns:
        str: The path of the created directory.
    """
    if isinstance(dir_path, str):
        dir_path = dir_path
    else:
        dir_path = os.getcwd()
    year_dir = os.path.join(dir_path, str(year))
    month_dir = os.path.join(year_dir, str(month))
    day_dir = os.path.join(month_dir, str(day))
    city_dir = os.path.join(day_dir, city)
    os.makedirs(city_dir, exist_ok=True)
    print(f'directories have been created with success: \nPath for new dir: {city_dir}')
    return city_dir


def save_weather_data_json(weather_data,
                           city_dir,
                           city,
                           current_date,
                           current_or_forecast = 'current'):
    """
    Save weather data in JSON format to a specified directory.

    Args:
        weather_data (dict): Weather data to be saved.
        city_dir (str): The directory path where the data should be saved.
        city (str): The name of the city.
        current_date (datetime): The date and time of data extraction.
        current_or_forecast (str): 'current' for current weather data, 'forecast' for forecast data.

    Returns:
        None
    """
    file_name = f'{current_or_forecast}_weather_{city}_{current_date.strftime("%Y-%m-%d_%H_%M_%S")}.json'
    file_path = os.path.join(city_dir, file_name)
    with open(file_path, 'w') as json_file:
        json.dump(weather_data, json_file, indent= 4)
    print(f'Data for the city: {city} has been saved in dir: {file_path}')


def create_current_date_directory_structure(city):
    """
    Create a directory structure based on the current date.

    Args:
        city (str): The name of the city.

    Returns:
        str: The path of the created directory.
    """
    date = datetime.now()
    year, month, day = date.year, date.month, date.day
    city_dir = create_directory_structure(year, month, day, city, dir_path= "")
    return city_dir


def save_file_and_create_dir_structure(city, weather_data, current_or_forecast= 'current' ):
    weather_data = weather_data[current_or_forecast]
    date = datetime.now()
    city_dir = create_current_date_directory_structure(city)
    save_weather_data_json(weather_data, city_dir, city, date, current_or_forecast)


def data_preprocessing(df, add_column_feature= 'last_updated', is_current_data= True):
    """
    Perform data preprocessing on a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to be preprocessed.
        add_column_feature (str): The name of the column to add.
        is_current_data (bool): True for current data, False for forecast data.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    warnings.filterwarnings("ignore")
    c_df = df[[add_column_feature] + features_list]
    if is_current_data:
        c_df = c_df.loc['text'::]
        c_df = c_df.reset_index(drop=True)
        c_df = c_df.rename(columns={add_column_feature: 'time'})
    c_df['time'] = pd.to_datetime(c_df['time'])
    c_df = c_df.assign(
        year=c_df['time'].dt.year,
        month=c_df['time'].dt.month,
        day=c_df['time'].dt.day,
        hour=c_df['time'].dt.hour,
        minute=c_df['time'].dt.minute,
        second=c_df['time'].dt.second
    )
    return c_df



