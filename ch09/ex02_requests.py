# p294

import requests

url = "http://quotesondesign.com/wp-json/posts"
resp = requests.get(url)
print(resp)
print(resp.text)
