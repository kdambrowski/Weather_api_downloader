import time

from sklearn.metrics import mean_absolute_error as MAE

from functions import *
from setings import cities, waiting_time

if __name__ == '__main__':
    filename = create_city_list_file("cities", cities)
    print_city_from_config_file(filename)

    cities = config_file_opener(filename)
    for city in cities:
        current_weather_data = get_weather_data(city, current_or_forecast= 'current')
        display_weather_info(city, current_weather_data)

    for city in cities:
        current_weather_data = get_weather_data(city, current_or_forecast= 'current')
        save_file_and_create_dir_structure(city, current_weather_data, current_or_forecast= 'current')

    for city in cities:
        forecast_weather_data = get_weather_data(city, current_or_forecast= 'forecast')
        save_file_and_create_dir_structure(city, forecast_weather_data, current_or_forecast= 'forecast')

    date = datetime.now()

    column_list_for_combined = []
    unique_columns = list(set(column_list_for_combined))
    combined_df = pd.DataFrame(columns= unique_columns)
    i = 0
    while i < 3:
        for city in cities:
            current_weather_data = get_weather_data(city, current_or_forecast='current')
            current_df = pd.DataFrame(current_weather_data['current'])
            curr_df = data_preprocessing(current_df, add_column_feature= 'last_updated', is_current_data= True)

            forecast_weather_data = get_weather_data(city, current_or_forecast= 'forecast')
            forecast_json = forecast_weather_data['forecast']
            fore_df = pd.DataFrame(forecast_json['forecastday'][0]['hour'])
            fore_df = data_preprocessing(fore_df, add_column_feature= 'time', is_current_data= False)

            current_hour = curr_df['hour'].iloc[0]
            fore_cast_series = fore_df[fore_df['hour'] == current_hour]
            diff_row = curr_df.iloc[0] - fore_cast_series.iloc[0]
            diff_df = pd.DataFrame([diff_row], columns= curr_df.columns)

            curr_df['city'] = city
            fore_cast_series['city'] = city
            diff_df['city'] = city
            curr_df['checking_index'] = i
            fore_cast_series['checking_index'] = i
            diff_df['checking_index'] = i
            curr_df['data_status'] = 'current'
            fore_cast_series['data_status'] = 'forecast'
            diff_df['data_status'] = 'difference'

            result_df = pd.concat([curr_df, fore_cast_series, diff_df])
            key_mapping = {0: 'current', 1: 'forecast', 2: 'difference curr-forecast'}
            result_df.reset_index(inplace=True, drop=True)
            result_df.index = result_df.index.map(key_mapping)

            column_list = result_df.columns.tolist()
            column_list.append(column_list_for_combined)
            combined_df = pd.concat([combined_df, result_df])
        time.sleep(waiting_time)
        i += 1

    combined_df.reset_index(drop=True, inplace=True)
    print(combined_df)

    numeric_columns = combined_df.select_dtypes(include=['int', 'float']).columns.tolist()
    value_col = numeric_columns[:5]
    real_value = combined_df[combined_df['data_status'] == 'current']
    pred_value = combined_df[combined_df['data_status'] == 'forecast']
    for column in value_col:
        y_pred = real_value[column]
        y_real = pred_value[column]
        mae_result = MAE(y_real, y_pred)
        print(f'MAE metric for feature {column} = {mae_result}')
