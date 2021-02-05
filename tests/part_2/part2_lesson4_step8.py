import time
import math

import clipboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'http://suninjuly.github.io/explicit_wait2.html'
time_to_wait_optimal_price = 12
txt_optimal_price = '$100'
txt_price_locator = '//h5[@id="price"]'  # css #price
btn_book_locator = '//button[@id="book"]'  # css button#book
txt_x_value_locator = '//span[@id="input_value"]'  # css #input_value
field_answer_locator = '//input[@id="answer"]'  # css #answer
btn_submit_locator = '//button[@id="solve"]'  # css button#solve


def x_value() -> int:
    return int(browser.find_element_by_xpath(txt_x_value_locator).text)


def compute_result(x: int) -> str:
    return str(math.log(abs(12 * math.sin(x))))


def wait_optimal_price():
    return WebDriverWait(browser, time_to_wait_optimal_price).until(
        EC.text_to_be_present_in_element((By.XPATH, txt_price_locator), txt_optimal_price)
    )


browser = webdriver.Chrome()
browser.get(url)

try:
    if wait_optimal_price():
        browser.find_element_by_xpath(btn_book_locator).click()
        formula_result = compute_result(x_value())
        browser.find_element_by_xpath(field_answer_locator).send_keys(formula_result)
        browser.find_element_by_xpath(btn_submit_locator).click()
        alert = browser.switch_to.alert
        answer = alert.text.split(' ')[-1]
        print(answer)  # For visual check
        clipboard.copy(answer)
        time.sleep(2)  # For visual check
        alert.accept()
    else:
        raise Exception('No optimal plan is shown')
finally:
    time.sleep(3)  # For visual check
    browser.quit()
