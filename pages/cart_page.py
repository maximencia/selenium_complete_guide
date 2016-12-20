# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_on_this_page(self):
        return len(self.driver.find_elements_by_id("box-login")) > 0

    def open(self):
        self.driver.get("http://localhost/litecart/en/checkout")
        return self

    def del_from_cart(self, product):
        order=self.driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']")
        #print("Total_order_distinct_prod:"+str(len(order)))

        for i in range(len(order)): #так как может быть случайно 2 раза один и тотже товар заказан надо искать уникальные
            self.driver.find_element_by_name('remove_cart_item').click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.staleness_of(order[0]))

    def del_all_from_cart(self):
        order=self.driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']")
        for i in range(len(order)): #так как может быть случайно 2 раза один и тотже товар заказан надо искать уникальные
            self.driver.find_element_by_name('remove_cart_item').click()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.staleness_of(order[0]))

