from selenium import webdriver
import os
import time


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Petr')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Popov')

    email = browser.find_element_by_name('email')
    email.send_keys('email')

    add_file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '../test.txt')
    add_file.send_keys(file_path)

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(10)
    browser.quit()

print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.join(current_dir, '../test.txt'))
