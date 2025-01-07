from datetime import datetime
import pytz
import requests
import streamlit as st
import folium
from streamlit_folium import folium_static

secret = st.secrets["MY_SECRET"]

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
        icon_url = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
        lat = data['coord']['lat']
        lon = data['coord']['lon']

        # Create a map centered at the coordinates
        weather_map = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker([lat, lon], popup=f"{city_name} Weather").add_to(weather_map)

        return (
        f"Weather in {city_name}:  \n Temperature: {temperature}°C   \n Humidity: {humidity}%   \n Condition: {weather_condition}",
        weather_map, icon_url)
    else:
        return "City not found.", None, None


def display_date_time(user_timezone, location_timezone=None):
    user_time = datetime.now(pytz.timezone(user_timezone))
    formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
    result = f"Your current date and time: {formatted_user_time}"

    if location_timezone:
        location_time = user_time.astimezone(pytz.timezone(location_timezone))
        formatted_location_time = location_time.strftime("%A, %B %d, %Y, %I:%M %p")
        result += f"\nDate and time in {location_timezone}: {formatted_location_time}"

    return result


# Streamlit UI
st.title('*Weather App*')

# Get city name input from the user
city_name = st.text_input('*Enter city name:*', key='city_input_1')

# Ensure city_name is defined and only proceed if it is not empty
if city_name:
    api_key = secret
    weather_info, weather_map, icon_url = get_weather(city_name, api_key)

    # Display the weather info
    st.write(weather_info)

    # Display the weather icon
    if icon_url:
        st.image(icon_url)

    # Display the map
    if weather_map:
        folium_static(weather_map)

# Display current date and time in Jerusalem
st.write(display_date_time("Asia/Jerusalem"))