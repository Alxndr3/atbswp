from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://nostarch.com')
html_element = browser.find_element_by_tag_name('html')
html_element.send_keys(Keys.END)  # Scrolls to bottom
sleep(1)
html_element.send_keys(Keys.HOME)  # Scrolls to top



# browser = webdriver.Firefox()
# browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv='
#             '13&ct=1600745647&rver=7.0.6737.0&wp=MBI_SSL&wreply='
#             'https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsC'
#             'srfState%3d89040ade-d6a0-b8d3-ab87-8cc878c68fc2&id=292841'
#             '&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
# email_element = browser.find_element_by_id('i0116')
# email_element.send_keys('xndr3@hotmail.com')
# email_button = browser.find_element_by_id('idSIButton9')
# sleep(1)
# email_button.click()
# sleep(1)
# password_element = browser.find_element_by_id('i0118')
# password_element.send_keys('Supaocl*')
# password_element.submit()


# Clicking the page
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# link_element = browser.find_element_by_link_text('Read Online for Free')
# print(type(link_element))
# link_element.click()


# Finding an element by class name.
# browser = webdriver.Firefox()
# browser.get('http://inventwithpython.com')
# try:
#     element = browser.find_element_by_class_name("col-sm-12")
#     print('Found <%s> element with that class name!' % element.tag_name)
# except Exception as ex:
#     print(f'{ex} Was not able to find an element with that name.')
# browser.close()
