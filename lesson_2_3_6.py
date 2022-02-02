from selenium import webdriver
import math
import time


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element_by_css_selector('.trollface.btn').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = int(browser.find_element_by_id('input_value').text)
    result = calc(number)

    response_field = browser.find_element_by_id('answer')
    response_field.send_keys(result)

    browser.find_element_by_class_name('btn').click()

    alert_text = browser.switch_to.alert.text
    print(alert_text.split(': ')[1])

finally:
    time.sleep(5)
    browser.quit()
