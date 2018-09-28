# p378

import requests

url = "https://raw.githubusercontent.com/AstinChoi/introducing-python/master/intro/top_rated.json"
response = requests.get(url)
data = response.json()
for video in data["feed"]["entry"][0:6]:
    print(video["title"]["$t"])
