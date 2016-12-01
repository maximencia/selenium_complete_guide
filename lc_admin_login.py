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



def find_and_fill_element(wd, element_name, value):
    wd.find_element_by_name(element_name).click()
    wd.find_element_by_name(element_name).clear()
    wd.find_element_by_name(element_name).send_keys(value)


# Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
#
# 1) входит в панель администратора http://localhost/litecart/admin
# 2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
# 3) для каждой страницы проверяет наличие заголовка

def test_admin_login(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.implicitly_wait(60)
    find_and_fill_element(wd,element_name="username",value="admin")
    find_and_fill_element(wd,element_name="password",value="admin")
    wd.find_element_by_name("login").click()
    #sleep(5)
    #p = wd.find_elements_by_xpath("//ul[@id='box-apps-menu']")

    #читаем основное меню
    l=wd.find_elements_by_xpath("//*[@id='app-']/a/span[2]")
    for i in range(len(l)):
        print
        #print (str(i)+".")
        t=wd.find_elements_by_xpath("//*[@id='app-']/a/span[2]")
        link_name=t[i].text
        print (str(i)+"."+link_name)
        #переходим к пункту основного меню
        t[i].click()
        #ищем пункты подменю
        wd.implicitly_wait(2)
        list_sub_menu=wd.find_elements_by_xpath("//ul[@class='docs']//li//span")
        print ("   "+str(len(list_sub_menu)))

        #print link_name
        #а заголовок в шапке можно получить так: driver.getTitle()
        #tt=wd.title
        #ttt=wd.find_element_by_xpath(".//*[@id='content']/h1").text
        #print tt
        #print ttt

        #ttt=wd.find_element_by_xpath("//title").text
        #print wd.find_element_by_xpath("//title").text
        # Максим Максим http://tonyganch.com/git/reset/