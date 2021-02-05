import time

from selenium import webdriver

url = 'http://suninjuly.github.io/huge_form.html'
field_input_locator = '//input'
btn_submit_locator = '//button[@class="btn btn-default"]'

browser = webdriver.Chrome()
browser.get(url)

try:
    all_fields = browser.find_elements_by_xpath(field_input_locator)

    for field in all_fields:
        field.send_keys('test')
    btn_submit = browser.find_element_by_xpath(btn_submit_locator)
    btn_submit.click()
    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(1)
    alert.accept()
    time.sleep(1)

finally:
    browser.quit()