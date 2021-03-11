import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
btn_add_to_basket_locator = "//form[@id='add_to_basket_form']/button[@type='submit']"


def test_check_add_to_basket_button(browser):
    browser.get(link)
    assert WebDriverWait(browser, timeout=5).until(expected_conditions.visibility_of_element_located((By.XPATH, btn_add_to_basket_locator)))
    assert browser.find_element_by_xpath(btn_add_to_basket_locator).is_displayed()
    time.sleep(3)  # To visual check
