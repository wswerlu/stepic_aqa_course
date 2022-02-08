link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basket_should_be_on_product_page(browser):
    # открываем страницу
    browser.get(link)
    # находим кнопку Добавить в корзину
    button_add_to_basket = browser.find_elements_by_class_name('btn-add-to-basket')
    # проверяем, что на странице есть кнопка для добавления товара в корзину и она только одна
    # p.s. сделал такую проверку, чтобы был хоть какой-то смысл в assert
    assert len(button_add_to_basket) == 1, 'Not button "Add to basket" or too much buttons'
