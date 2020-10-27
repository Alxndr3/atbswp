#! /bin/env python3
# lucky_search.py - Opens several Google search results.
import requests
import sys
import webbrowser
import re
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print('Type what you\'d like to search after the script name.')
    sys.exit()

# To get all arguments passed to sys.argv as it was one only string.
search = ' '.join(sys.argv[1:])
print('Googling...')
source = requests.get(f'https://google.com/search?q={search}')
source.raise_for_status()
# Make the soup object.
soup = BeautifulSoup(source.text, features='lxml')
#
link_open = 0
for div_link in soup.find_all('div', class_="ZINbbc xpd O9g5cc uUPGi"):
    source = div_link.a.get('href')
    # Regular expression to pick the right peace of the link.
    regex = re.compile(r'(http.*?)(&sa=)')
    my_link = regex.findall(source)
    # To limit the searches in five.
    if link_open >= 6:
        break
    for link in my_link:
        print(f'Opening link: {link[0]}')
        webbrowser.open(link[0])
    link_open += 1
