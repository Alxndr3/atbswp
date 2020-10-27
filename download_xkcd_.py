#! /bin/env python3
# download_xkcd.py - Downloads every single XKCD comic.
import os
import requests
from bs4 import BeautifulSoup


# Load XKCD home page.
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

# Download the page.
source = requests.get(url)
source.raise_for_status()
#  Find the URL of the comic image.
soup = BeautifulSoup(source.text, features='lxml')
comic_element = soup.select('#comic img')
if comic_element == list():
    print('Could not find comic image.')
else:
    print(comic_element)
    print(comic_element[0].get('title'))
