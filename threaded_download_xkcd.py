#! /usr/bin/env python3
# threaded_downlaod_xkcd.py - Multithreadly downloads every single XKCD comic.
import os
import requests
import threading
from bs4 import BeautifulSoup



os.makedirs('xkcd', exist_ok=True) # Store comics in ./xkcd

def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        print('Downloadin page https://xkcd.com/%s...' %(url_number))

        res = requests.get('https://xkcd.com/%s' % (url_number))
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comic_element = soup.select('#comic img')

        if comic_element == []:
            print('Could not find comic image.')
        else:
            comic_url = comic_element[0].get('src')

        # Download  the image.
        print('Downloading image %s...' % (comic_url))
        res = requests.get('https:' + comic_url)
        res.raise_for_status()


       # Save the image to ./xkcd.
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:

           for chunk in res. iter_content(100000):
               image_file.write(chunk)

           image_file.close()


#  Create and start the Thread objects.
download_threads = list() # a list of all thread objects.
for i in range(0, 140, 10): # loops 14 times, creates 14 threads.
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so set it to 1.

    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for download_thread in download_threads:
    download_thread.join()
print('Done.')

