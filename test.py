import requests
from bs4 import BeautifulSoup

uri = 'https://www.stitchfiddle.com/en'

r = requests.get(uri)

html = r.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")
print(soup.decode(pretty_print=True))
