import wacky_beer as wb
import wacky_beer as wb
import requests
from bs4 import BeautifulSoup
import json

urls = wb.beer_styles_urls()
soup = wb.bs_soup(urls[0][1])
soup = BeautifulSoup(requests.get(urls[0][1]).content, 'html.parser')
bs_id = json.loads(soup.find(id = 'wpp-json').get_text())['ID']