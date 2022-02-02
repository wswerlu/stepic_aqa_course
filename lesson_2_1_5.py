from selenium import webdriver
import time
import math


def calc(item):
    return str(math.log(abs(12 * math.sin(int(item)))))


link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    value = browser.find_element_by_id('input_value').text
    answer = calc(value)

    response_field = browser.find_element_by_id('answer')
    response_field.send_keys(answer)

    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()

    sub_button = browser.find_element_by_class_name('btn')
    sub_button.click()

finally:
    time.sleep(15)
    browser.quit()
