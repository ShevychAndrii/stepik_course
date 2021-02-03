import math
import time

from selenium import webdriver

url = 'http://suninjuly.github.io/math.html'
txt_x_value_locator = '//span[@id="input_value"]'  # css #input_value
field_answer_locator = '//input[@id="answer"]'  # css #answer
checkbox_locator = '//input[@type="checkbox"]'  # css [type="checkbox"]
radiobutton_locator = '//input[@id="robotsRule"]'  # css #robotsRule
btn_submit_locator = '//button[@type="submit"]'  # css .btn


def get_x_value():
    return browser.find_element_by_xpath(txt_x_value_locator).text


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get(url)

try:
    math_result = calc(get_x_value())
    browser.find_element_by_xpath(field_answer_locator).send_keys(math_result)
    checkbox = browser.find_element_by_xpath(checkbox_locator)
    checkbox.click()
    assert checkbox.is_selected()
    radiobutton = browser.find_element_by_xpath(radiobutton_locator)
    radiobutton.click()
    assert radiobutton.is_selected()
    browser.find_element_by_xpath(btn_submit_locator).click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(2)
    browser.quit()
