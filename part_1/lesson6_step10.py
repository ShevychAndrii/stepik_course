from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# url = 'http://suninjuly.github.io/registration1.html'
url = 'http://suninjuly.github.io/registration2.html'

field_first_name_locator = '//div[@class="first_block"]//input[@class="form-control first"]'  # css .first_block .first
field_last_name_locator = '//div[@class="first_block"]//input[@class="form-control second"]'  # css .first_block .second
field_email_locator = '//div[@class="first_block"]//input[@class="form-control third"]'  # css .first_block .third
field_phone_locator = '//div[@class="second_block"]//input[@class="form-control first"]'  # css .second_block .first
field_address_locator = '//div[@class="second_block"]//input[@class="form-control second"]'  # css .second_block .second
btn_submit_locator = '//button[@type="submit"]'  # css .btn
txt_congrats_locator = '//h1'


def test_registration_only_with_required_fields():
    field_first_name = browser.find_element_by_xpath(field_first_name_locator)
    field_first_name.send_keys('John')
    field_last_name = browser.find_element_by_xpath(field_last_name_locator)
    field_last_name.send_keys('Doe')
    field_email = browser.find_element_by_xpath(field_email_locator)
    field_email.send_keys('test@yopmail.com')
    btn_submit = browser.find_element_by_xpath(btn_submit_locator)
    btn_submit.click()
    assert WebDriverWait(browser, timeout=3).until(ec.presence_of_element_located((By.XPATH, txt_congrats_locator)))
    assert browser.find_element_by_xpath(txt_congrats_locator).text \
        == 'Congratulations! You have successfully registered!'


try:
    browser = webdriver.Chrome()
    browser.get(url)

    test_registration_only_with_required_fields()

finally:
    browser.quit()
