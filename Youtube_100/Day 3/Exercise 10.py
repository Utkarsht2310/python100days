import requests
import json

query = input("Enter the topic: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-11-26&sortBy=publishedAt&apiKey=ea59c959611d43a9aadc1d3a908ec753"
r = requests.get(url)
# print(r.text)
news = json.loads(r.text)
print(news, type(news))


# my_api_key = "ea59c959611d43a9aadc1d3a908ec753"

