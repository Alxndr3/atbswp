from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = Firefox()
driver.implicitly_wait(30)
driver.get('https://gabrielecirulli.github.io/2048/')
area = driver.find_element_by_tag_name('body')
for x in range(1, 10):
    sleep(1)
    area.send_keys(Keys.ARROW_UP)
    area.send_keys(Keys.ARROW_RIGHT)
    area.send_keys(Keys.ARROW_DOWN)
    area.send_keys(Keys.ARROW_LEFT)
