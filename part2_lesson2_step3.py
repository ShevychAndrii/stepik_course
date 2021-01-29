import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

url_1 = 'http://suninjuly.github.io/selects1.html'
url_2 = 'http://suninjuly.github.io/selects2.html'

value1_locator = '//span[@id="num1"]'  # css #num1
value2_locator = '//span[@id="num2"]'  # css #num2
dropdown_locator = '//select[@id="dropdown"]'  # css #dropdown
btn_submit_locator = '//button[@type="submit"]'  # css .btn


def value_x() -> int:
    return int(browser.find_element_by_xpath(value1_locator).text)


def value_y() -> int:
    return int(browser.find_element_by_xpath(value2_locator).text)


def result_sum() -> str:
    return str(value_x() + value_y())


def choose_element_by_value(value: str):
    dropdown = Select(browser.find_element_by_xpath(dropdown_locator))
    dropdown.select_by_value(value)


browser = webdriver.Chrome()
browser.get(url_1)

try:
    choose_element_by_value(value=result_sum())
    browser.find_element_by_xpath(btn_submit_locator).click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(3)
    browser.quit()
