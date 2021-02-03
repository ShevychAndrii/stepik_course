import math
import time

import clipboard
from selenium import webdriver

url = 'http://suninjuly.github.io/alert_accept.html'
btn_i_want_locator = '//button[@type="submit"]'  # css button.btn
txt_x_value_locator = '//span[@id="input_value"]'  # css #input_value
field_answer_locator = '//input[@id="answer"]'  # css #answer
btn_submit_locator = '//button[@type="submit"]'  # css button.btn


def value() -> int:
    return int(browser.find_element_by_xpath(txt_x_value_locator).text)


def compute_result(x_value: int) -> str:
    return str(math.log(abs(12 * math.sin(x_value))))


browser = webdriver.Chrome()
browser.get(url)

try:
    browser.find_element_by_xpath(btn_i_want_locator).click()
    browser.switch_to.alert.accept()
    formula_result = compute_result(value())
    browser.find_element_by_xpath(field_answer_locator).send_keys(formula_result)
    browser.find_element_by_xpath(btn_submit_locator).click()
    result = browser.switch_to.alert.text.split(' ')[-1]
    clipboard.copy(result)  # Copy result from alert to clipboard

finally:
    time.sleep(2)  # For visual check
    browser.quit()
