# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class ProductListPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    def add_in_cart (self, product):


        # self.driver.find_element_by_css_selector("[id ^= select2-country_code]").click()
        # self.driver.find_element_by_css_selector(".select2-results__option[id $= %s" % country).click()
        self.driver.find_element_by_xpath(".//*[@id='box-most-popular']//a[@class='link' and @title='Green Duck']").click()
        time.sleep(1)
        self.driver.find_element_by_name('add_cart_product').click()

        wait=WebDriverWait(self.driver,10)
        quantity_product_in_cart_now=1
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH,".//*[ @ id = 'cart']//a//span[@class='quantity']"),str(quantity_product_in_cart_now)))
        #вот тут как раз и ждем что поменяется свойство текст у элемента а потом щелкаем по главной странице
        self.driver.get("http://localhost/litecart/en/")



    # @property
    # def customer_rows(self):
    #     return self.driver.find_elements_by_css_selector("table.dataTable tr.row")
    #
    # def get_customer_ids(self):
    #     return set([e.text for e in self.customer_rows])
