import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

api_key = "ac2261df167c06bd38f816369574afa5"
city = input("Enter city name: ")
weather_data = get_weather_data(city, api_key)

temperature = weather_data['main']['temp']
weather_condition = weather_data['weather'][0]['description']
humidity = weather_data['main']['humidity']
print(f"Temperature: {temperature}°C\nWeather: {weather_condition}\nHumidity: {humidity}%")
