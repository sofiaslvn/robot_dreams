import requests
import random

websites = [
    "http://www.google.com",
    "http://www.facebook.com",
    "http://www.twitter.com",
    "http://www.amazon.com",
    "http://www.apple.com"
]


def request():
    random_site = random.choice(websites)
    response = requests.get(random_site)

    print("Назва сайту:", random_site)
    print("Статус-код відповіді:", response.status_code)
    print("Довжина HTML-коду:", len(response.text))


request()