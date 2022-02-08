from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element_by_id('book').click()

    number = int(browser.find_element_by_id('input_value').text)
    result = calc(number)

    response_field = browser.find_element_by_id('answer')
    response_field.send_keys(result)

    browser.find_element_by_id('solve').click()

    alert_text = browser.switch_to.alert.text
    print(alert_text.split(': ')[1])

finally:
    browser.quit()
