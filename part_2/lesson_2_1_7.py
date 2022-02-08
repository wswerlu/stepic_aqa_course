from selenium import webdriver
import time
import math


def calc(item):
    return str(math.log(abs(12 * math.sin(int(item)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    chest = browser.find_element_by_id('treasure')
    value = chest.get_attribute('valuex')
    answer = calc(value)

    response_field = browser.find_element_by_id('answer')
    response_field.send_keys(answer)
    time.sleep(1)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    time.sleep(1)

    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    time.sleep(1)

    sub_button = browser.find_element_by_class_name('btn')
    sub_button.click()

finally:
    time.sleep(15)
    browser.quit()
