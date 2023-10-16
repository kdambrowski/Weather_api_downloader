# Weather Data Processing and Analysis

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Status](#project-status)
- [Acknowledgements](#acknowledgements)

## Overview
The Weather Data Processing and Analysis project is a Python-based tool for collecting, processing and analyzing weather data. It allows users to retrieve weather information from an external API, save it in a structured format, and perform data analysis, including calculating the Mean Absolute Error (MAE) for various weather features.

## Technologies Used
- Python
- Pandas
- Requests
- NumPy
- scikit-learn
- JSON
- os

## Features
- Retrieves weather data for specified cities from an external API.
- Creates a directory structure for storing weather data.
- Saves weather data in JSON format for further analysis.
- Performs data preprocessing for both current and forecast data.
- Calculates MAE for selected weather features.
- Provides an easy-to-use interface for obtaining and analyzing weather data.

## Setup
To run the project, follow these steps:

1. Install the required libraries by executing the following command in your terminal:

```bash
pip install -r requirements.txt
```

2. Customize the settings in the provided `setings.py` file according to your requirements.

3. Run the main script using the following command in your terminal:

```bash
python3 main.py
```

4. Observe and utilize the generated weather data and analysis results.

## Usage
1. Clone the project repository to your local machine.

2. Install the required libraries as mentioned in the "Setup" section.

3. Customize the settings in the `setings.py` file according to your needs.

4. Run the project using Python.

5. Observe the directories with saved weather data and the calculated MAE metrics.

## Project Status
The project is complete and ready for use. You can retrieve weather data, save it, and perform data analysis with ease.

## Acknowledgements
- This project was developed using Python and various libraries that make weather data processing and analysis more accessible and user-friendly.
