from selenium import webdriver
import math
import time


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    number = int(browser.find_element_by_id('input_value').text)
    result = calc(number)

    response_field = browser.find_element_by_id('answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", response_field)
    response_field.send_keys(result)

    browser.find_element_by_css_selector('[for="robotCheckbox"]').click()

    browser.find_element_by_css_selector('[for="robotsRule"]').click()

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(15)
    browser.quit()
