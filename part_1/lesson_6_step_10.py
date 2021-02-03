import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://suninjuly.github.io/registration2.html'

field_first_name_locator = '.first_block .first'
field_last_name_locator = '.first_block .second'
field_email_locator = '.first_block .third'
btn_submit_locator = '.btn'
txt_congrats_locator = 'h1'


def test_registration_only_with_required_fields():
    field_first_name = browser.find_element_by_css_selector(field_first_name_locator)
    field_first_name.send_keys('John')
    field_last_name = browser.find_element_by_css_selector(field_last_name_locator)
    field_last_name.send_keys('Doe')
    field_email = browser.find_element_by_css_selector(field_email_locator)
    field_email.send_keys('test@yopmail.com')
    btn_submit = browser.find_element_by_css_selector(btn_submit_locator)
    btn_submit.click()
    assert \
        WebDriverWait(browser, timeout=3).until(ec.presence_of_element_located((By.CSS_SELECTOR, txt_congrats_locator)))
    assert browser.find_element_by_css_selector(txt_congrats_locator).text \
        == 'Congratulations! You have successfully registered!'


try:
    browser = webdriver.Chrome()
    browser.get(url)

    test_registration_only_with_required_fields()

finally:
    time.sleep(3)  # For visual check
    browser.quit()
