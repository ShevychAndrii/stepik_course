import time

from selenium import webdriver

url = 'http://suninjuly.github.io/find_xpath_form'

field_first_name_locator = '//input[@name="first_name"]'
field_last_name_locator = '//input[@name="last_name"]'
field_city_locator = '//input[@class="form-control city"]'
field_country_locator = '//input[@id="country"]'
btn_submit_locator = '//button[@type="submit"]'

browser = webdriver.Chrome()
browser.get(url)

try:
    field_fist_name = browser.find_element_by_xpath(field_first_name_locator).send_keys('Ivan')
    field_last_name = browser.find_element_by_xpath(field_last_name_locator).send_keys('Petrov')
    field_city = browser.find_element_by_xpath(field_city_locator).send_keys('Saratov')
    field_country = browser.find_element_by_xpath(field_country_locator).send_keys('Russia')
    btn_submit = browser.find_element_by_xpath(btn_submit_locator).click()

    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(.5)
    alert.accept()
    time.sleep(.5)

finally:
    browser.quit()
