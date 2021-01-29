import math
import time

from selenium import webdriver

url = 'http://suninjuly.github.io/find_link_text'
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = webdriver.Chrome()
browser.get(url)

try:
    link = browser.find_element_by_link_text(link_text)
    link.click()
    # field_first_name = browser.find_element_by_xpath('//input[@name="first_name"]')
    field_first_name = browser.find_element_by_css_selector('[name="first_name"]')
    field_first_name.send_keys('Ivan')
    # field_last_name = browser.find_element_by_xpath('//input[@name="last_name"]')
    field_last_name = browser.find_element_by_css_selector('[name="last_name"]')
    field_last_name.send_keys('Petrov')
    # field_city = browser.find_element_by_xpath('//input[@class="form-control city"]')
    field_city = browser.find_element_by_css_selector('.city')
    field_city.send_keys('Smolensk')
    # field_country = browser.find_element_by_xpath('//input[@id="country"]')
    field_country = browser.find_element_by_css_selector('#country')
    field_country.send_keys('Russia')
    # btn_submit = browser.find_element_by_xpath('//button')
    btn_submit = browser.find_element_by_css_selector('.btn')
    btn_submit.click()

finally:
    time.sleep(15)
    browser.quit()
