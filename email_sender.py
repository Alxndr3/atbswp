import os
from selenium import webdriver
from time import sleep


email_address = os.environ.get('EMAIL_ADDRESS_H')
email_pass = os.environ.get('EMAIL_PASS_H')

browser = webdriver.Firefox()

browser.implicitly_wait(10)

browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv='
            '13&ct=1600745647&rver=7.0.6737.0&wp=MBI_SSL&wreply='
            'https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsC'
            'srfState%3d89040ade-d6a0-b8d3-ab87-8cc878c68fc2&id=292841'
            '&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')

email_element = browser.find_element_by_id('i0116')
email_element.send_keys(email_address)

email_button = browser.find_element_by_id('idSIButton9')
sleep(1)
email_button.click()
sleep(1)
password_element = browser.find_element_by_id('i0118')
sleep(1)
password_element.send_keys(email_pass)
password_element.submit()
sleep(1)
stay_button = browser.find_element_by_id('idBtn_Back')
stay_button.click()
browser.get('https://outlook.live.com/mail/0/inbox')
sleep(2)
message_button = browser.find_element_by_id('id__3')
assert isinstance(message_button, object)
message_button.click()
to_element = browser.find_element_by_css_selector('.ms-BasePicker-input')
to_element.send_keys('alxndr3@gmail.com')
to_element.click()  
subject_element = browser.find_element_by_id('TextField100')
subject_element.send_keys('Hello Universe')
subject_element = browser.find_element_by_css_selector('._4utP_vaqQ3UQZH0GEBVQe')
subject_element.send_keys('Hello Universe')
send_button = browser.find_element_by_id('id__104')
send_button.click()
browser.close()

