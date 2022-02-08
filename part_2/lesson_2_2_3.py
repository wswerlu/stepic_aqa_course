from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    first_number = int(browser.find_element_by_id('num1').text)
    second_number = int(browser.find_element_by_id('num2').text)
    sum_of_numbers = first_number + second_number

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(sum_of_numbers))
    time.sleep(1)

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(15)
    browser.quit()
