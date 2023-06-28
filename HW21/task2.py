import requests

def get_city_coordinates(city_name):
    geocoding_api_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }
    response = requests.get(geocoding_api_url, params=params)
    data = response.json()
    if "results" in data:
        result = data["results"][0]
        latitude = result["latitude"]
        longitude = result["longitude"]
        return latitude, longitude
    return None, None

def get_current_weather(city_name):
    latitude, longitude = get_city_coordinates(city_name)
    if latitude is None or longitude is None:
        print("Failed to get coordinates for the city.")
        return

    weather_api_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true"
    }
    response = requests.get(weather_api_url, params=params)
    data = response.json()
    if "current_weather" in data:
        current_weather = data["current_weather"]
        print("Current Weather in", city_name)
        print("Temperature:", current_weather["temperature"], "°C")
    else:
        print("Failed to get current weather for the city.")

city = input("Введіть назву міста: ")
get_current_weather(city)