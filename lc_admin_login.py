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
        print len(sticker)
        sticker_sum=sticker_sum+len(sticker)

    assert len(duck_crowd) == sticker_sum



#1) на странице http://localhost/litecart/admin/?app=countries&doc=countries
#а) проверить, что страны расположены в алфавитном порядке
#б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке
def test_countries(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.implicitly_wait(60)
    find_and_fill_element(wd,element_name="username",value="admin")
    find_and_fill_element(wd,element_name="password",value="admin")
    wd.find_element_by_name("login").click()

    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    #Найдем список стран .//table[@class='dataTable']//tr[@class='row']//td[5]
    countries=wd.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']//td[5]")
    zones_count=wd.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']//td[6]")
    country_acronym=wd.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']//td[4]")
    country_list=[]
    geo_zones__index=[]
    #print len(countries)
    for country in countries:
        country_list.append(country.text)
        print country.text
    sorted_country_list=sorted(country_list)
    assert country_list==sorted_country_list
    #Найдем список стран .//table[@class='dataTable']//tr[@class='row']//td[5]


    #http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=CA
    #http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US