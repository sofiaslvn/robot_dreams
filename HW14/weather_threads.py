# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
# Реалізувати за допомогою модуля requests з використанням мультипотоковості і мультипроцесорності.
# 2. Знайти середню температуру по прогнозу для кожного міста і вивести в якому місті зараз найспекотніше.
# 3. Вивести різницю по часу виконання програми використовуючи потоки і процеси.

import requests
import threading
import time

cities = [
    {"name": "Kyiv", "latitude": 50.45, "longitude": 30.52},
    {"name": "Ternopil", "latitude": 49.55, "longitude": 25.59},
    {"name": "Lviv", "latitude": 49.84, "longitude": 24.02},
    {"name": "Odessa", "latitude": 46.49, "longitude": 30.74},
    {"name": "Poltava", "latitude": 49.59, "longitude": 34.55}
]

def get_weather(city):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['latitude']}&longitude={city['longitude']}&hourly=temperature_2m"
    response = requests.get(url)
    temperature = response.json()["hourly"]["temperature_2m"][0]
    return temperature

start = time.time()
threads = []
temperatures = []
for city in cities:
    thread = threading.Thread(target=get_weather, args=(city,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for city in cities:
    temperature = get_weather(city)
    temperatures.append(temperature)
    print(f"City: {city['name']}, Temperature: {temperature}°C")

hottest_city = max(cities, key=get_weather)
print(f"The hottest city is {hottest_city['name']}")
end = time.time()
result = end - start
print(f"Multithread time is {result}")



