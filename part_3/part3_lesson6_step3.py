import math
import time

import clipboard
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

urls = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']

field_answer_locator = '//textarea'
btn_send_locator = '//button[@class="submit-submission"]'
txt_optional_feedback_locator = '//pre[@class="smart-hints__hint"]'

feedback_messages = list()


def answer() -> str:
    return str(math.log(int(time.time())))


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', urls)
def test_check_the_feedback(browser, url):
    browser.get(url)
    assert WebDriverWait(browser, timeout=5).until(expected_conditions.visibility_of_element_located((By.XPATH, field_answer_locator)))
    browser.find_element_by_xpath(field_answer_locator).send_keys(answer())
    browser.find_element_by_xpath(btn_send_locator).click()
    assert WebDriverWait(browser, timeout=5).until(expected_conditions.visibility_of_element_located((By.XPATH, txt_optional_feedback_locator)))
    text_feedback = browser.find_element_by_xpath(txt_optional_feedback_locator).text
    assert text_feedback == 'Correct!', feedback_messages.append(text_feedback)


def test_process_feedback_messages():
    result = ' '.join([str(elem).strip() for elem in feedback_messages])
    clipboard.copy(result)
