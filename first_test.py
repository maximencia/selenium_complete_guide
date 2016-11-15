# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class first_test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_(self):
        success = True
        wd = self.wd

        wd.get("http://software-testing.ru/lms/")
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("maxim.rumyantsev")
        time.sleep(10)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

