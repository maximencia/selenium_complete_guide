# -*- coding: utf-8 -*-
import pytest,string,random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def wd(request):

    caps = DesiredCapabilities.CHROME
    #caps['loggingPrefs'] = {'performance': 'ALL'}
    caps['loggingPrefs'] = {'browser': 'ALL'}
    #caps['loggingPrefs'] = {'browser': 'INFO'}

    driver = webdriver.Chrome(desired_capabilities=caps)
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
    print()
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
            print()
    print (link_array)
    print (h1_array)
    assert (link_array)==(h1_array)

#задание 9
#1) на странице http://localhost/litecart/admin/?app=countries&doc=countries
#а) проверить, что страны расположены в алфавитном порядке
#б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить,
# что зоны расположены в алфавитном порядке
def test_geo_zones(wd,zones_page,flag):
    if flag == 1:
        wd.get("http://localhost/litecart/admin/login.php")
        wd.implicitly_wait(60)
        find_and_fill_element(wd,element_name="username",value="admin")
        find_and_fill_element(wd,element_name="password",value="admin")
        wd.find_element_by_name("login").click()

    #wd.get("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US")
    wd.get(zones_page)
    #получим все зоны
    rows=wd.find_elements_by_xpath(".//*[@id='table-zones']//tr [not(contains (@class, 'header'))]")
    #print ('123123'+str(len(rows)))
    i=0
    zones_name=[]
    for elements in rows:
        # теперь пробежим по столбцам текущего tr из цикла
            column_z = elements.find_elements_by_tag_name("td")
            zones_name.append(column_z[2].text)
    # удалим последний элемент. list.pop([i]), потому что это поле используется для фильтров
    # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
    zones_name.pop()
    #print
    print (zones_name)
    sorted_zones_list = sorted(zones_name)
    #print(sorted_zones_list)
    assert zones_name==sorted_zones_list

def test_geo_zones_local(wd):
    test_geo_zones(wd,"http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=US",1)
    test_geo_zones(wd,"http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code=CA",1)

def test_countries(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.implicitly_wait(60)
    find_and_fill_element(wd,element_name="username",value="admin")
    find_and_fill_element(wd,element_name="password",value="admin")
    wd.find_element_by_name("login").click()

    #откроем страницу
    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    # Найдем список стран .//table[@class='dataTable']//tr[@class='row']//td[5]
    country_list = []
    zones_count=[]
    country_acronym=[]
    index_for_link=[]
    rows = wd.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']")
    #rows = wd.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row' and position() <= 39]")
    i=0
    for elements in rows:
    # теперь пробежим по столбцам текущего tr из цикла
        column = elements.find_elements_by_tag_name("td")
        country_list.append(column[4].text)
        zones_count.append(column[5].text)
        country_acronym.append(column[3].text)
        if int(column[5].text) >0:
            index_for_link.append(i)
        i=i+1
    #сравним список стран и отсортированный список
    sorted_country_list = sorted(country_list)
    assert country_list==sorted_country_list
    #print() print (country_list) print (zones_count) print (country_acronym) print print (index_for_link)
    for i in index_for_link:
        #print (country_acronym[i]) print(country_list[i]) print(zones_count[i])
        zone_page =("http://localhost/litecart/admin/?app=countries&doc=edit_country&country_code="+str(country_acronym[i]))
        test_geo_zones(wd,zone_page,flag=0)

#задание 9
# на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
# зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке
def test_geo_zones_page(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.implicitly_wait(60)
    find_and_fill_element(wd,element_name="username",value="admin")
    find_and_fill_element(wd,element_name="password",value="admin")
    wd.find_element_by_name("login").click()
    wd.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    #зайти в каждую из стран
    geozones_list_text=[]
    #множество из ссылок на страницы с зонами
    geo_links=wd.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a")
    for link in geo_links:
        print(link.get_attribute('href'))
        geozones_list_text.append(link.get_attribute('href'))
        # запоминаем ссылки в спец массив для того чтобы селениум при переключении и обновлении страницы нам ничего не попротил
        # и небыло ошибки типа python Message: stale element reference: element is not attached to the page document

    #далее бежим уже по спискам в открытых страничках
    for i in range(len(geozones_list_text)):
        geozones_list=[] #обнулим список
        wd.get(geozones_list_text[i])
        geo_zones_in_selects = wd.find_elements_by_xpath(".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,'true'))]/option[@selected='selected']")
        for geozones in geo_zones_in_selects:
            geozones_list.append(geozones.text)

        sorted_geozones_list = sorted(geozones_list)
        print(geozones_list)
        assert geozones_list == sorted_geozones_list


domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains): return random.choice(domains)
def get_random_name(letters, length): return ''.join(random.choice(letters) for i in range(length))
def generate_random_emails(nb, length): return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]
def generate_mail(): return (generate_random_emails(1, 7))


def test_new_product_add(wd):
        wd.get("http://localhost/litecart/admin/login.php")
        wd.implicitly_wait(60)
        find_and_fill_element(wd,element_name="username",value="admin")
        find_and_fill_element(wd,element_name="password",value="admin")
        wd.find_element_by_name("login").click()

        name_of_new_prod=get_random_name(letters,10)

        wd.find_element_by_link_text("Catalog").click()
        wd.find_element_by_link_text("Add New Product").click()

        wd.find_element_by_css_selector("label").click()
        if not wd.find_element_by_name("status").is_selected():
            wd.find_element_by_name("status").click()

        find_and_fill_element(wd,element_name='name[en]',value=name_of_new_prod)
        find_and_fill_element(wd,element_name='code',value='3')
        find_and_fill_element(wd,element_name='quantity',value='10')
        find_and_fill_element(wd,element_name='new_images[]',value='c:\selenium_complete_guide\data\duck_image.png')
    #   find_and_fill_element(wd,element_name='date_valid_from',value='02 12 2015') - вот так не работает!!! потому что
        # нельзя clear делать
        wd.find_element_by_name('date_valid_from').click()
        wd.find_element_by_name('date_valid_from').send_keys('2015-12-12')
        wd.find_element_by_name('date_valid_to').click()
        wd.find_element_by_name('date_valid_to').send_keys('2017-12-12')
    #    find_and_fill_element(wd,element_name='date_valid_to',value='2017-12-12')

        wd.find_element_by_link_text("Information").click()
        if not wd.find_element_by_xpath(
            "//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]").is_selected():
            wd.find_element_by_xpath(
            "//div[@id='tab-information']//select[normalize-space(.)='-- Select -- ACME Corp.']//option[2]").click()

        find_and_fill_element(wd,element_name='keywords',value='my_duck')
        find_and_fill_element(wd,element_name='short_description[en]',value='my_duck')

        wd.find_element_by_link_text("Prices").click()

        wd.find_element_by_name("purchase_price").send_keys("22")
        if not wd.find_element_by_xpath("//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='tab-prices']/table[1]/tbody/tr/td/select//option[2]").click()

        find_and_fill_element(wd,element_name='prices[USD]', value='23')

        wd.find_element_by_name("save").click()
        wd.find_element_by_id("content").click()

        #проверим что товар появился на странице просто сравнив его имя
        #http: // localhost / litecart / admin /?app = catalog & doc = catalog
        wd.find_element_by_link_text("Catalog").click()
        test="//a[text()='"+str(name_of_new_prod)+"']"
        assert_element = wd.find_elements_by_xpath(test)
        print (len(assert_element))
        assert len(assert_element)==1


# Задание 14. Проверьте, что ссылки открываются в новом окне
# Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.
#
# Сценарий должен состоять из следующих частей:
#
# 1) зайти в админку
# 2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
# 3) открыть на редактирование какую-нибудь страну или начать создание новой
# 4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой --
# они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.
#
# Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank".
# Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне,
# потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.
#
# Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна.
from contextlib import contextmanager

@contextmanager #https://docs.python.org/2.7/library/contextlib.html
def wait_for_new_window(driver, timeout=10): #http://stackoverflow.com/questions/26641779/python-selenium-how-to-wait-for-new-window-opens
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))

def test_ext_links(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.implicitly_wait(60)
    find_and_fill_element(wd, element_name="username", value="admin")
    find_and_fill_element(wd, element_name="password", value="admin")
    wd.find_element_by_name("login").click()
    print()

    wd.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    wd.find_element_by_xpath(".//*[@id='content']/div/a").click()
    all_ex_link=wd.find_elements_by_xpath(".//*[@id='content']/form/table[1]//a[@target='_blank']")
    print("Total ext_link: "+ str(len(all_ex_link)))

    # получаем    набор    дескрипторов    текущих    открытых    окон
    main_window = wd.current_window_handle
    print('main_window')
    print(main_window)
    old_windows = wd.window_handles
    print('old_windows')
    print(old_windows)
    # нажимаем    на    ссылку, которая    открывает    документ    в    новом    окне
    #wd.findElement(By.tagName("a")).click();
    for j in range (10):                         #нагрузим
        for i in range (len(all_ex_link)):
            print("i="+str(i))
            with wait_for_new_window(wd,10):
                all_ex_link[i].click()
            #sleep(3)
            # здесь    нужно    будет    дождаться    открытия    нового    окна    \

            # получаем новый    набор    дескрипторов, включающий    уже    и    новое    окно
            new_windows = wd.window_handles
            print('new_windows')
            print(new_windows)
            # получаем     дескриптор    нового    окна (из одного списка вычтем другой)
            new_window = list(set(new_windows).difference(old_windows))
            print('new_window')
            print(new_window)
            #закроем новое окно
            wd.switch_to_window(new_window[0])
            wd.close()
            wd.switch_to_window(main_window)
            #sleep(5)  без слипов на platform win32 -- Python 3.5.2, pytest-3.0.4, py-1.4.31, pluggy-0.4.0 за 16 сек отработало


# Задание 17. Проверьте отсутствие ошибок в логе браузера
# Сделайте сценарий, который проверяет, не появляются ли сообщения об ошибках при открытии страниц в учебном приложении, а именно -- страниц товаров в каталоге в административной панели.
#
# Сценарий должен состоять из следующих частей:
#
# 1) зайти в админку
# 2) открыть каталог, категорию, которая содержит товары (страница http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1)
# 3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения об ошибках (любого уровня критичности)
#
# Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def check_exists_by_xpath(wd,xpath):
    try:
        #wait = WebDriverWait(wd, 10)
        #wait.until(EC.staleness_of(order[0]))
        wd.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_xpath2(wd,xpath):
    return len(wd.find_elements_by_xpath(xpath)) == 0
#
# ...wait_for_new_windowwd.implicitly_wait(1)
#     while  check_exists_by_xpath(wd,".//td[./i[@class='fa fa-folder' and @style='color: #cccc66; margin-left: 32px;']]"):
#         print (check_exists_by_xpath(wd,".//td[./i[@class='fa fa-folder' and @style='color: #cccc66; margin-left: 32px;']]"))
#         i=i+1
#         print(i)
#         #not_open_folder=wd.find_elements_by_xpath(".//td[./i[@class='fa fa-folder' and @style='color: #cccc66; margin-left: 32px;']]")
#         #not_open_folder.find_elements_by_xpath("./a").click()
#         #print(len(not_open_folder))
#
## тяжелый случай - алексей говорит нужно ожидать не отсутсвие элемента
# а присутсвие того элемента который подтверждает отсутствие первого
## Будем думать а пока сделаем по другому.

import re
def test_error_in_browsers_log(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.implicitly_wait(60)
    find_and_fill_element(wd, element_name="username", value="admin")
    find_and_fill_element(wd, element_name="password", value="admin")
    wd.find_element_by_name("login").click()
    print()

    wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    #wd.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")#  у меня товаров в корне больше.
    #[23:11:50] maxim rumyantsev: Алексей подскажите нужно ли мучатся с подкаталогами в задание про логирование,
    #  или достаточно прокликать только товары лежащие в корне.
    #[23:12:11] Alexei Barantsev: подкаталоги не нужно
    #тогда проще
    #найдем все ссылки с товарами и будем кликать последовательно
    links=wd.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[./img and ./a]/a")
    links_count=len(links)

    print (wd.log_types)

    for i in range(links_count):
        links = wd.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[./img and ./a]/a")
        print(links[i].get_attribute('href'))
        text3 = re.sub(r'http:\/\/localhost\/litecart\/admin\/\?app=catalog\&doc=edit_product\&', '_', links[i].get_attribute('href'),flags=re.IGNORECASE)
        text4 = re.sub(r'\&', '_', text3, flags=re.IGNORECASE)
        page_name = re.sub(r'=', '_', text4, flags=re.IGNORECASE)

        links[i].click()
        print(i)
        for l in wd.get_log("browser"):
            print(l)
        #перформанс показывает:
        #for entry in wd.get_log('performance'):
        #    print (entry)

        #сделаем еще скрин для утяжеления:
        screen_path=str("c:\\selenium_complete_guide\\temp\\"+str(i)+'_'+page_name+".jpg")
        wd.get_screenshot_as_file(screen_path)
        wd.find_element_by_name("cancel").click()

    #
    # КАК НАПОЛУЧАТЬ ОШИБОК В ЛОГ:
    # Коллеги, у    меня    перфоманс    выводится    а    ошибок    никаких    не    дает.Задание    про    логирование.
    # О ! mySql    выключил    в    процессе.Потом    тесты    и    mySql - перезапустил - теперь    показывает.    Ошибся
    # я.Тут    ктото    советовал    сеть    отключить! Так    я    отключил    и    забыл    про    нее - по    началу    все
    # работало.А    теперь    чтото    типо    {'level': 'SEVERE',
    #  'message': 'http://browser-update.org/update.js - Failed to load resource: net::ERR_INTERNET_DISCONNECTED',
    #  'source': 'network', 'timestamp': 1482097637480}
    # :)
    print(u'ГОТОВО')