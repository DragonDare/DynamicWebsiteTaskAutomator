from bs4 import BeautifulSoup   #Web Scraper
from urllib.request import urlopen  #URL fetch
import re   #Regular Expressions

url = "https://github.com/html5lib/"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)