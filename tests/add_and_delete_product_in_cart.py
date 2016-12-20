# -*- coding: utf-8 -*-
import pytest,string,random
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

@pytest.fixture
def wd(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def find_and_fill_element(wd, element_name, value):
    wd.find_element_by_name(element_name).click()
    wd.find_element_by_name(element_name).clear()
    wd.find_element_by_name(element_name).send_keys(value)


def test_add_prod_to_cart(wd):
    print()
    wd.get("http://localhost/litecart/en/")
    wd.implicitly_wait(60)


    for i in range(1,4):  #
        print(str(i)+'.')
        #выберем товар на угад и добавим его в таблицу
        duck_crowd = wd.find_elements_by_xpath(".//ul[@class='listing-wrapper products']//li")
        print("Total count of ducks:" + str(len(duck_crowd)))
        random_index=random.randint(0, len(duck_crowd)-1)
        print("Index of random item:"+str(random_index))
        go= duck_crowd[random_index].find_element_by_xpath("./a[@class='link']").click()
        wd.find_element_by_name('add_cart_product').click()

        wait=WebDriverWait(wd,10)

        element = wait.until(EC.text_to_be_present_in_element((By.XPATH,".//*[ @ id = 'cart']//a//span[@class='quantity']"),str(i)))
        #вот тут как раз и ждем что поменяется свойство текст у элемента а потом щелкаем по главной странице
        wd.get("http://localhost/litecart/en/")

    #открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
    wd.get("http://localhost/litecart/en/checkout")
    order=wd.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']")
    print("Total_order_distinct_prod:"+str(len(order)))

    for i in range(len(order)): #так как может быть случайно 2 раза один и тотже товар заказан надо искать уникальные
        wd.find_element_by_name('remove_cart_item').click()
        wait = WebDriverWait(wd, 10)
        wait.until(EC.staleness_of(order[0]))
        #если .//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class="unit-cost"] есть то элементы еще остались.
        #sleep(1)

# app/application.py
# model/custumer.py -> product.py +
# pages/ 3 страницы
#                  product_list_page.py
# test/
