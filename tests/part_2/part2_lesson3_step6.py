import math
import time

import clipboard
from selenium import webdriver

url = 'http://suninjuly.github.io/redirect_accept.html'
btn_i_want_locator = '//button[@type="submit"]'  # css button.btn
txt_x_value_locator = '//span[@id="input_value"]'  # css #input_value
field_answer_locator = '//input[@id="answer"]'  # css #answer
btn_submit_locator = '//button[@type="submit"]'  # cs button.btn


def x_value() -> int:
    return int(browser.find_element_by_xpath(txt_x_value_locator).text)


def compute_result(x: int) -> str:
    return str(math.log(abs(12 * math.sin(x))))


browser = webdriver.Chrome()
browser.get(url)

try:
    browser.find_element_by_xpath(btn_i_want_locator).click()
    browser.switch_to.window(browser.window_handles[1])
    formula_result = compute_result(x_value())
    browser.find_element_by_xpath(field_answer_locator).send_keys(formula_result)
    browser.find_element_by_xpath(btn_submit_locator).click()
    alert = browser.switch_to.alert
    answer = alert.text.split(' ')[-1]
    print(answer)  # For visual check
    time.sleep(2)  # For visual check
    alert.accept()
    clipboard.copy(answer)

finally:
    browser.quit()
