import os
import time

import clipboard
from selenium import webdriver

url = 'http://suninjuly.github.io/file_input.html'
field_first_name_locator = '//input[@name="firstname"]'  # css [name="firstname"]
field_last_name_locator = '//input[@name="lastname"]'  # css [name="lastname"]
field_email_locator = '//input[@name="email"]'  # css [name="email"]
btn_choose_file_locator = '//input[@id="file"]'  # css #file
btn_submit_locator = '//button[@type="submit"]'  # css .btn
short_bio_path = f'{os.path.dirname(__file__)}/data/short_bio.txt'

browser = webdriver.Chrome()
browser.get(url)

try:
    browser.find_element_by_xpath(field_first_name_locator).send_keys('Jon')
    browser.find_element_by_xpath(field_last_name_locator).send_keys('Doe')
    browser.find_element_by_xpath(field_email_locator).send_keys('jon.doe@yopmail.com')
    browser.find_element_by_xpath(btn_choose_file_locator).send_keys(short_bio_path)
    browser.find_element_by_xpath(btn_submit_locator).click()
    result = browser.switch_to.alert.text.split(' ')[-1]
    clipboard.copy(result)

finally:
    time.sleep(2)
    browser.quit()
