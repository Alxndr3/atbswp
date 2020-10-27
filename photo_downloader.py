import requests
import os
from selenium import webdriver


search_term = str(input('Download photos of: '))
os.makedirs('imgur', exist_ok=True)
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
driver.get('https://imgur.com')
driver.implicitly_wait(30)

search_bar = driver.find_element_by_css_selector('.Searchbar-textInput')
search_bar.send_keys(search_term)
search_bar.submit()

images = driver.find_elements_by_tag_name('img')

for x in range(len(images)):
    img = images[x]
    photo_url = img.get_attribute('src')
    print(photo_url)

    print(os.path.basename(photo_url))
    # print(f'Downloading: {photo_url}')

    res = requests.get(photo_url)
    res.raise_for_status()

    with open(os.path.join('imgur', os.path.basename(photo_url)), 'wb') as image_file:
        for chunk in res.iter_content(100000):
            image_file.write(chunk)


