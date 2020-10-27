from selenium.webdriver import Firefox
import requests
import os


# os.makedirs('link_checker_downloads', exist_ok=True)
page = 'https://automatetheboringstuff.com/'

driver = Firefox()
driver.implicitly_wait(30)
driver.get(page)

for t in driver.find_elements_by_tag_name('a'):
    link = t.get_attribute('href')
    if link == None:
        continue
    print(link)
    if requests.get(link).status_code == 404:
        print(f'Bronken link: {link} conde: {requests.get(link).status_code}')
    else:

driver.close()

