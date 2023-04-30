import requests
import multiprocessing
import time

cities2 = [
    {"name": "Kyiv", "latitude": 50.45, "longitude": 30.52},
    {"name": "Ternopil", "latitude": 49.55, "longitude": 25.59},
    {"name": "Lviv", "latitude": 49.84, "longitude": 24.02},
    {"name": "Odessa", "latitude": 46.49, "longitude": 30.74},
    {"name": "Poltava", "latitude": 49.59, "longitude": 34.55}
]
def get_temperature(city):
    url2 = f"https://api.open-meteo.com/v1/forecast?latitude={city['latitude']}&longitude={city['longitude']}&hourly=temperature_2m"
    response2 = requests.get(url2)
    temperature2 = response2.json()["hourly"]["temperature_2m"][0]
    city_temperature = f"City: {city['name']}, Temperature: {temperature2}°C"
    print(city_temperature)
    return temperature2

start = time.time()
if __name__ == '__main__':
    # start_time = time.time()
    with multiprocessing.Pool() as pool:
        temperatures = pool.map(get_temperature, cities2)
    # end_time = time.time()

    hottest_city = cities2[temperatures.index(max(temperatures))]
    print(f"The hottest city is {hottest_city['name']}")
    # result2 = end_time - start_time
result2 = time.time() - start

print(f"Multiprocessing time: {result2} seconds.")
