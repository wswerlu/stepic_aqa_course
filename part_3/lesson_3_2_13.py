import unittest
from selenium import webdriver


class TestWelcomeText(unittest.TestCase):
    def test_registration_1(self):
        browser = webdriver.Chrome()
        link_1 = "http://suninjuly.github.io/registration1.html"

        browser.get(link_1)

        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys('First_Name')
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys('Second_Name')
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys('Email')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)

        browser.quit()

    def test_registration_2(self):
        browser = webdriver.Chrome()
        link_2 = "http://suninjuly.github.io/registration2.html"

        browser.get(link_2)

        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys('First_Name')
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys('Second_Name')
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys('Email')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text)

        browser.quit()


if __name__ == "__main__":
    unittest.main()
