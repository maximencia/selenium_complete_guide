# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@pytest.fixture
def wd(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


# Задание 8. Сделайте сценарий, проверяющий наличие стикеров у товаров
    # Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на
    # главной странице. Стикеры -- это полоски в левом верхнем углу изображения товара, на которых написано
    # New или Sale или что-нибудь другое. Сценарий должен проверять, что у каждого товара имеется ровно один стикер.

def test_sticker_verify(wd):
    wd.get("http://localhost/litecart/en/")
    wd.implicitly_wait(60)
    #.//ul[@class="listing-wrapper products"]//li
    #найдем всех уточек на странице. Их должно быть 11.
    sticker_sum=0
    duck_crowd=wd.find_elements_by_xpath(".//ul[@class='listing-wrapper products']//li")
    print ("Total count of ducks:"+str(len(duck_crowd)))
    #теперь будем искать в каждой утке наклейку:
    for duck in duck_crowd:
        sticker=duck.find_elements_by_xpath(".//div[starts-with(@class,'sticker')]")
        print (len(sticker))
        sticker_sum=sticker_sum+len(sticker)

    assert len(duck_crowd) == sticker_sum