import streamlit as st
import requests
from datetime import datetime
import pytz

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = data['weather'][0]
        temperature = main_data['temp']
        humidity = main_data['humidity']
        weather_condition = weather_data['description']
        return (f"Weather in {city_name}: \n Temperature: {temperature}°C  \n Humidity: {humidity}% \n Condition: {weather_condition}")
    else:
        return "City not found."

def display_date_time(user_timezone, location_timezone=None):
    user_time = datetime.now(pytz.timezone(user_timezone))
    formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
    result = f"Your current date and time: {formatted_user_time}"

    if location_timezone:
        location_time = user_time.astimezone(pytz.timezone(location_timezone))
        formatted_location_time = location_time.strftime("%A, %B %d, %Y, %I:%M %p")
        result += f"\nDate and time in {location_timezone}: {formatted_location_time}"

    return result

st.title('Weather App')
city_name = st.text_input('Enter city name:')
api_key = "ac2261df167c06bd38f816369574afa5"
user_timezone = 'America/New_York'
city_timezone = 'Europe/London'

if city_name:
    weather_info = get_weather(city_name, api_key)
    st.write(weather_info)

st.write(display_date_time("Asia/Jerusalem"))

st.write("The end")