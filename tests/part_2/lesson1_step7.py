import math
import time

from selenium import webdriver


url = 'http://suninjuly.github.io/get_attribute.html'
img_chest_locator = '//img[@id="treasure"]'  # css #treasure
field_answer_locator = '//input[@id="answer"]'  # css #answer
checkbox_robot_locator = '//input[@id="robotCheckbox"]'  # css #robotCheckbox
radiobutton_robots_locator = '//input[@id="robotsRule"]'  # css #robotsRule
btn_submit_locator = '//button[@type="submit"]'  # css .btn


def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


def x_value() -> str:
    return browser.find_element_by_xpath(img_chest_locator).get_attribute('valuex')


browser = webdriver.Chrome()
browser.get(url)

try:
    math_result = calc(x_value())
    browser.find_element_by_xpath(field_answer_locator).send_keys(math_result)
    checkbox_robot = browser.find_element_by_xpath(checkbox_robot_locator)
    checkbox_robot.click()
    assert checkbox_robot.is_selected()
    assert checkbox_robot.get_attribute('checked')
    radiobutton_robots = browser.find_element_by_xpath(radiobutton_robots_locator)
    radiobutton_robots.click()
    assert radiobutton_robots.is_selected()
    assert radiobutton_robots.get_attribute('checked')
    btn_submit = browser.find_element_by_xpath(btn_submit_locator)
    assert btn_submit.is_enabled()
    btn_submit.click()
    print(browser.switch_to.alert.text)

finally:
    time.sleep(2)
    browser.quit()
