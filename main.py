"""Real-Time Weather Detection  Application"""
# Author: Paila Jeevan
# TODO: Flipkart Internship Task
import requests
import os
import csv
from datetime import datetime  # important import


# Centralize configuration to avoid duplicate lines
API_KEY = os.environ.get("OPENWEATHER_API_KEY", "4efc678ccdbd3cb455da8478d3aa3d3e")  # OpenWeather API key
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather" #URI for weather data


def request(city: str): # Function to interact with OpenWeatherMap API
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    try:
        resp = requests.get(WEATHER_URL, params=params)  # requesting weather data from OpenWeatherMap API
    except Exception as e:
        print("\n Error:", str(e))
        return None

    if resp.status_code == 200:# Successful response
        return resp.json() # Converting the text response into JSON format
    else:
        print("\n City not found or API error")
    return None


def information(city: str):
    data = request(city)
    if not data:
        return
    # Converting the text response into JSON format already done in helper
    print(f"\nWeather in {city.title()}:")  # show the city name
    print(f" Temperature: {data['main']['temp']}°C")  # show temperature
    print(f" Feels Like: {data['main']['feels_like']}°C")  # show feels like temperature
    print(f" Condition: {data['weather'][0]['description'].capitalize()}")  # show weather condition
    print(f" Humidity: {data['main']['humidity']}%")  # show humidity
    print(f" Wind Speed: {data['wind']['speed']} m/s")  # show wind speed


# Storing Weather data in CSV file
def store(city: str):
    data = request(city)
    if not data:
        return

    city_name = data["name"]  # Store city name into city_name variable
    country = data["sys"]["country"]  # store country code into country variable
    temperature = data["main"]["temp"]  # store temperature into temperature variable
    feels_like = data["main"]["feels_like"]  # store feels like temperature into feels_like variable
    humidity = data["main"]["humidity"]  # store humidity into humidity variable
    condition = data["weather"][0]["description"].capitalize()  # store weather condition into condition variable
    wind_speed = data["wind"]["speed"]  # store wind speed into wind_speed variable

    filename = "weather_data.csv"  # CSV file name to store weather data
    file_exists = os.path.isfile(filename)  # Checking the file is already exists or not
    with open(filename, mode="a", newline="", encoding="utf-8") as file:  # Open the file for appending data
        writer = csv.writer(file)  # Creating a csv writer object to write the data
        if not file_exists:  # If the file is not already exists, write the header
            writer.writerow(
                [
                    "Timestamp","City","Country","Temperature (°C)","Feels Like (°C)","Humidity (%)","Condition", "Wind Speed (m/s)",
                ]
            )  # Writing the header row in this format in csv file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow(
            [timestamp, city_name, country, temperature, feels_like, humidity, condition, wind_speed]
        )  # Writing the weather data get for api file into csv file
    print(f"\n Weather data for {city_name} stored in {filename}")
class WeatherApp:
    """Simple wrapper class to interact with the weather helper functions."""

    def run(self):
        city = input("Enter City: ")  # Get city name from user
        information(city)  # Show weather info
        store(city)  # Store data in CSV


if __name__ == "__main__":
    app = WeatherApp()
    app.run()
    # Tested with cities: Guntur, Delhi, London, New York, Tokyo