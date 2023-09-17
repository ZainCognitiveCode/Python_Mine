import requests
import json
query = input("what type of news are you interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-13&sortBy=publishedAt&apiKey=437d6122272b4921b71d49e28f34ce92"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("................................")
    