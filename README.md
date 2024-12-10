# WeatherForecastApplication-
For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

The **Weather Forecast Application** is a Python-based tool that allows users to fetch current weather data for any location. It uses the **OpenWeatherMap API** to retrieve data such as temperature, humidity, wind speed, and weather description. 

# Weather Forecast Application (Basic Version)

## Overview

The **Weather Forecast Application** is a Python-based tool that allows users to fetch current weather data for any location. It uses the **OpenWeatherMap API** to retrieve data such as temperature, humidity, wind speed, and weather description. The application includes a simple and user-friendly **Tkinter GUI** to input a location, fetch weather details, and display them interactively.

## Features

- **Real-time Weather Data**: Fetch current weather details for any location worldwide.
- **User-friendly Interface**: A clean GUI built with Tkinter for easy navigation and interaction.
- **Export to CSV**: Save the fetched weather details to a CSV file for further analysis.

## Folder Structure


## Project Structure

```
WeatherForecastApp/
├── data/                         
│   ├── sample_data/              # Folder for storing sample weather data
├── gui/                          
│   ├── __init__.py               # Initializes the GUI module
│   ├── weather_gui.py            # GUI implementation for the application
├── utils/                        
│   ├── __init__.py               # Initializes the utils module
│   ├── weather_api.py            # Fetch weather data using OpenWeatherMap API
│   ├── export_csv.py             # Logic for exporting data to CSV
├── main.py                       # Main entry point for the application
├── requirements.txt              # Dependencies required for the project
├── README.md                     # Documentation for the project
```


## Installation and Setup

### Prerequisites

Make sure the following software is installed on your system:

- **Python 3.8+**: Download Python from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package manager (comes with Python by default).

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/thekartikeyamishra/WeatherForecastApp.git
   cd WeatherForecastApp
'''
2. Set Up Virtual Environment Create and activate a virtual environment to isolate dependencies:

On **Windows**:
   ```bash
python -m venv .venv
.venv\Scripts\activate
```
On **macOS/Linux**:
```bash
python -m venv .venv
source .venv/bin/activate
```
3. Install Dependencies Install the required Python packages:

```bash
pip install -r requirements.txt
```
4. Add OpenWeatherMap API Key :
 - Sign up at OpenWeatherMap and get your free API key.
 - Replace YOUR_OPENWEATHERMAP_API_KEY in utils/weather_api.py with your API key.

5. Run the Application Execute the main script to launch the application:

```bash
python main.py
```

###How to Use
- Launch the application by running main.py.
- Enter a location (city name) in the input field.
- Click on the "Fetch Weather" button to retrieve weather data.
- View the fetched weather details in the text box.
- To save the data, click on the "Export to CSV" button.
