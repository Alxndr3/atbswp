#! /bin/env python3
# download_xkcd.py - Downloads every single XKCD comic.
import os
import requests
from bs4 import BeautifulSoup


# Load XKCD home page.
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    # Download the page.
    print('Downloading the page %s...' % url)
    source = requests.get(url)
    source.raise_for_status()
    #  Find the URL of the comic image.
    soup = BeautifulSoup(source.text, features='lxml')
    comic_element = soup.select('#comic img')
    if comic_element == list():
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_element[0].get('src')
    # Download the image.
        print('Downloading image %s...' % comic_url)
        res = requests.get(comic_url)
        res.raise_for_status()
    # Save the image to ./skcd.
    with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
    # Get the prev button URL
    prev_link = soup.select('a[rel="prev"]')[0]
    prev_href = prev_link.get('href')
    url = 'http://xkcd.com' + prev_link.get('href')
print('Done.')
