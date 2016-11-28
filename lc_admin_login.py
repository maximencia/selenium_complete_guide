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

#chrome
        ##chrome_driver = webdriver.Chrome #(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
        #options = Options()
        #options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        ##options.add_argument("start-maximized")
        #options.add_argument("--start-fullscreen")

#ie
        #ie_driver = webdriver.Ie()

#ff
        # простая схема, которую я использовал ранее с текущей версией FF = 50
        #firefox_driver = webdriver.Firefox

        # Попробуйте запустить разработанный ранее сценарий логина в браузере Firefox ESR 45,
        # используя старую схему запуска, без использования geckodriver.
        # Если Selenium не может сам найти место, куда установлен Firefox ESR -- укажите в параметрах запуска путь к браузеру.

        #firefox_driver = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
        #firefox_driver = webdriver.Firefox(firefox_binary="c:\\Program Files\\Nighlty\\firefox.exe") selenium.common.exceptions.WebDriverException: Message: Failed to start browser:
        #получилось только с версией href="https://archive.mozilla.org/pub/firefox/nightly/latest-mozilla-central/firefox-53.0a1.en-US.win32.installer.exe
        firefox_driver = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Nightly\\firefox.exe")
                                                           #"c:\\Program Files (x86)\\Nightly\\firefox.exe"
        # firefox_driver = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla_Firefox_ESR\\firefox.exe")

        # # новая схема:
        # wd = webdriver.Firefox()
        # # новая схема более явно:
        # firefox_driver= webdriver.Firefox(capabilities={"marionette": True})
        # # старая схема:
        # firefox_driver = webdriver.Firefox(capabilities={"marionette": False})
        #
        #self.wd = chrome_driver(chrome_options=options)
        #self.wd = ie_driver
        self.wd = firefox_driver
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
        time.sleep(5)
        #wd.find_element_by_link_text("Appearence").click()
        #wd.find_element_by_link_text("Catalog").click()
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
