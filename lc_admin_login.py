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
    print
    #sleep(5)
    #p = wd.find_elements_by_xpath("//ul[@id='box-apps-menu']")
    link_array=[]
    h1_array=[]
    #читаем основное меню
    mm=wd.find_elements_by_xpath("//*[@id='app-']/a/span[2]") # количество пунктов
    for i in range(len(mm)):
        # как только мы кликаем по ссылке - страница меняется и то что было в mm_l становится не актуальным
        #  - так что ищем список заного и выбираем нужный элемент по индексу.
        mm_el=wd.find_elements_by_xpath("//*[@id='app-']/a/span[2]")
        link_name=mm_el[i].text # имя пункта главного меню
        print (str(i)+"."+link_name)
        #переходим к пункту основного меню
        mm_el[i].click()

        #ищем пункты подменю
        wd.implicitly_wait(1)
        sub_menu=wd.find_elements_by_xpath("//ul[@class='docs']//li//span")
        print ("   Total subsmenu elements:"+str(len(sub_menu)))

        if len(sub_menu)<1:
            head_title=wd.find_element_by_xpath(".//*[@id='content']/h1").text
            print("Main Link_text  : "+link_name)
            print("     Head_title : "+head_title)
            link_array.append(link_name)
            h1_array.append(head_title)
        for j in range(len(sub_menu)):
            sub_menu_el=wd.find_elements_by_xpath("//ul[@class='docs']//li//span")
            sub_menu_el[j].click()
            # эх - после клика нужно все перечитывать!
            #найдем пункт меню и h1
            sub_menu_el=wd.find_elements_by_xpath("//ul[@class='docs']//li//span")
            sub_m_link_name=sub_menu_el[j].text # имя пункта главного меню
            head_title2=wd.find_element_by_xpath(".//*[@id='content']/h1").text
            print("     Link_text  : "+sub_m_link_name)
            print("     Head_title : "+head_title2)
            link_array.append(sub_m_link_name)
            h1_array.append(head_title2)
            print
    print (link_array)
    print (h1_array)
    assert (link_array)==(h1_array)
