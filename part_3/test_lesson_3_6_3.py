import pytest
from selenium import webdriver
import math
import time


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


parts_of_link = ['236895', '236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']


@pytest.mark.parametrize('part_of_link', parts_of_link)
def test_feedback_is_correct(browser, part_of_link):
    link = f'https://stepik.org/lesson/{part_of_link}/step/1'
    # открываем браузер
    browser.get(link)
    # находим поле для ответа и вставляем в него ответ
    response_field = browser.find_element_by_class_name('ember-text-area')
    response_field.send_keys(str(math.log(int(time.time()))))
    # находим кнопку Отправить и кликаем по ней
    browser.find_element_by_class_name('submit-submission').click()
    # получаем текст фидбэка
    feedback = browser.find_element_by_class_name('smart-hints__hint').text

    assert feedback == 'Correct!', f'Feedback is "{feedback}"'
