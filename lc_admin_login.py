# -*- coding: utf-8 -*-
#from selenium.webdriver.firefox.webdriver import WebDriver
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_admin_login(unittest.TestCase):
    def setUp(self):
        chrome_driver = webdriver.Chrome #(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})

        options = Options()
        options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        #options.add_argument("start-maximized")
        options.add_argument("--start-fullscreen")

        #ie_driver = webdriver.Ie()
        #firefox_driver = webdriver.Firefox()

        self.wd = chrome_driver(chrome_options=options)
        #self.wd = ie_driver
        #self.wd = firefox_driver
        #self.wd = webdriver()
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
        time.sleep(3)
        wd.find_element_by_link_text("Appearence").click()
        wd.find_element_by_link_text("Catalog").click()
        # wd.find_element_by_link_text("Product Groups").click()
        # wd.find_element_by_link_text("Option Groups").click()
        # wd.find_element_by_link_text("Manufacturers").click()
        # wd.find_element_by_link_text("Countries").click()
        # wd.find_element_by_link_text("Catalog").click() #  - пока проверки не делаем.

        #Список Capabilities https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
        #wd = webdriver.Ie(capabilities={"unexpectedAlertBehaviour": "dismiss"})
        print(wd.capabilities)

        self.assertTrue(success)

    def find_and_fill_element(self, wd, element_name, value):
        wd.find_element_by_name(element_name).click()
        wd.find_element_by_name(element_name).clear()
        wd.find_element_by_name(element_name).send_keys(value)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
