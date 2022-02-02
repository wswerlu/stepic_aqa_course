from selenium import webdriver
import math
import time


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element_by_class_name('btn').click()

    browser.switch_to.alert.accept()

    number = int(browser.find_element_by_id('input_value').text)
    result = calc(number)

    response_field = browser.find_element_by_id('answer')
    response_field.send_keys(result)

    browser.find_element_by_class_name('btn').click()
    
finally:
    time.sleep(10)
    browser.quit()
