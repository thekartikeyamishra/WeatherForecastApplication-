import requests

API_KEY = "API Keys goes here !"

def fetch_weather(location):
    url= f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()
        weather ={
            "Location": data["name"],
            "Temperature (in C)": data["main"]["temp"],
            "Humidity % ": data["main"]["humidity"],
            "Wind Speed (m/s)": data["weather"][0]["description"].capitalize()
        }
        return weather
    return None