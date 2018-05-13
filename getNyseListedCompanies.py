import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.nyse.com/listings_directory/stock")
print(r.status_code)
#print(r.text)
print(r.headers.get("content-type", "unknown"))

