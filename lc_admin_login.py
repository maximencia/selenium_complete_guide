# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_admin_login(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def find_and_fill_element(self, wd, element_name, value):
        wd.find_element_by_name(element_name).click()
        wd.find_element_by_name(element_name).clear()
        wd.find_element_by_name(element_name).send_keys(value)

    def test_admin_login(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/litecart/admin/login.php")
        self.find_and_fill_element(wd,element_name="username",value="admin")
        self.find_and_fill_element(wd,element_name="password",value="admin")
        wd.find_element_by_name("login").click()
        #time.sleep(5)
        wd.find_element_by_link_text("Appearence").click()
        wd.find_element_by_link_text("Catalog").click()
        wd.find_element_by_link_text("Product Groups").click()
        wd.find_element_by_link_text("Option Groups").click()
        wd.find_element_by_link_text("Manufacturers").click()
        wd.find_element_by_link_text("Countries").click()
        wd.find_element_by_link_text("Catalog").click() #  - пока проверки не делаем.

        self.assertTrue(success)

    def find_and_fill_element(self, wd, element_name, value):
        wd.find_element_by_name(element_name).click()
        wd.find_element_by_name(element_name).clear()
        wd.find_element_by_name(element_name).send_keys(value)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
