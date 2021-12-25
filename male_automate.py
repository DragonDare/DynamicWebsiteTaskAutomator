from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://github.com/html5lib/"

page = "try1.html"

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)