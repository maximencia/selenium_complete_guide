# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import string,random

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

# Задание 10. Проверить, что открывается правильная страница товара
# Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.
# 1) Открыть главную страницу
# 2) Кликнуть по первому товару в категории Campaigns
# 3) Проверить, что открывается страница правильного товара
# Более точно, проверить, что
# а) совпадает текст названия товара
# б) совпадает цена (обе цены)
# Кроме того, проверить стили цены на главной странице и на странице товара -- первая цена серая, зачёркнутая, маленькая, вторая цена красная жирная, крупная.

def test_item_of_product_verify(wd):
    wd.get("http://localhost/litecart/en/")
    wd.implicitly_wait(60)
    #упрощенный вариант - Кликнуть по первому товару в категории Campaigns -  значит ограничим условие
    duck_crowd=wd.find_elements_by_xpath("//div[@id='box-campaigns']//ul[@class='listing-wrapper products']//li")
    #нужно сохранить аттрибуты товара для последующей проверки

    num_of_product=[]
    link_for_product_page=[]
    product_name=[]
    product_price=[]
    product_price_with_discount=[]

    product_price_style_text_decoration=[]
    product_price_style_font_size=[]
    product_price_with_discount_style_font_weight=[]
    product_price_with_discount_style_font_size=[]

    i=0
    for duck in duck_crowd:
        num_of_product.append(i)
        link_for_product_page.append(duck.find_element_by_xpath(".//a[@class='link']").get_attribute('href'))
        product_name.append(duck.find_element_by_xpath(".//div[@class='name']").text)
        # <div class="price-wrapper">
        #     <s class="regular-price">$20</s>
        #     <strong class="campaign-price">$18</strong>
        # </div>
        product_price.append(duck.find_element_by_xpath(".//div[@class='price-wrapper']/s").text)
        #тут нужно включать проверку на то что скидки может не быть.
        product_price_with_discount.append(duck.find_element_by_xpath(".//strong[@class='campaign-price']").text)
        #работа со стилями
        product_price_style_text_decoration.append(duck.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('text-decoration'))
        product_price_style_font_size.append(duck.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('font-size'))
        product_price_with_discount_style_font_weight.append(duck.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight'))
        product_price_with_discount_style_font_size.append(duck.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-size'))

        print('ELEMENT'+str(i))
        print(product_name)
        print(product_price)
        print(product_price_with_discount)
        print(product_price_style_text_decoration)
        print(product_price_style_font_size)
        print(product_price_with_discount_style_font_weight)
        print(product_price_with_discount_style_font_size)
        i=i+1

    print(link_for_product_page)
    #перейдем по ссылке для сравнения каждого товара
    for j in range(len(num_of_product)):
        wd.get(link_for_product_page[j])
        # проведем сравнение
        n_product_name=wd.find_element_by_xpath(".//*[@id='box-product']/div[1]/h1").text
        n_product_price=wd.find_element_by_xpath(".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/s").text
        #тут нужно включать проверку на то что скидки может не быть.
        n_product_price_with_discount=wd.find_element_by_xpath(".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/strong").text
        #работа со стилями
        n_product_price_style_text_decoration=wd.find_element_by_xpath(".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/s").value_of_css_property('text-decoration')
        n_product_price_style_font_size=wd.find_element_by_xpath(".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/s").value_of_css_property('font-size')
        n_product_price_with_discount_style_font_weight=wd.find_element_by_xpath(".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/strong").value_of_css_property('font-weight')
        n_product_price_with_discount_style_font_size=wd.find_element_by_xpath(".//*[@id='box-product']//div[@class='information']//div[@class='price-wrapper']/strong[@class='campaign-price']").value_of_css_property('font-size')

    print('ELEMENT FROM PRODUCT_PAGE')
    print(n_product_name)

    print(n_product_price)
    print(n_product_price_with_discount)

    print(n_product_price_style_text_decoration)
    print(n_product_price_style_font_size)
    print(n_product_price_with_discount_style_font_weight)
    print(n_product_price_with_discount_style_font_size)

    assert n_product_name == product_name[j]

    assert n_product_price == product_price[j]
    assert n_product_price_with_discount == product_price_with_discount[j]

    assert n_product_price_style_text_decoration == product_price_style_text_decoration[j]
    assert n_product_price_style_font_size == product_price_style_font_size[j]
    assert n_product_price_with_discount_style_font_weight == product_price_with_discount_style_font_weight[j]
    assert n_product_price_with_discount_style_font_size == product_price_with_discount_style_font_size[j]

# Задание 11. Сделайте сценарий регистрации пользователя
# Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart (не в админке, а в клиентской части магазина).
#
# Сценарий должен состоять из следующих частей:
#
# 1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты
# (чтобы не конфликтовало с ранее созданными пользователями),
# 2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
# 3) повторный вход в только что созданную учётную запись,
# 4) и ещё раз выход.

#Проверки можно никакие не делать, только действия -- заполнение полей, нажатия на кнопки и ссылки.
# Если сценарий дошёл до конца, то есть созданный пользователь смог выполнить вход и выход -- значит создание прошло успешно.

#В форме регистрации есть капча, её нужно отключить в админке учебного приложения на вкладке Settings -> Security.
def find_and_fill_element(wd, element_name, value):
    wd.find_element_by_name(element_name).click()
    wd.find_element_by_name(element_name).clear()
    wd.find_element_by_name(element_name).send_keys(value)

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains): return random.choice(domains)
def get_random_name(letters, length): return ''.join(random.choice(letters) for i in range(length))
def generate_random_emails(nb, length): return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]
def generate_mail(): return (generate_random_emails(1, 7))

def test_new_subscriber_registration(wd):
    #подготовим рандомный mail
    mail=generate_mail()
    wd.get("http://localhost/litecart/en/")
    wd.implicitly_wait(60)
    wd.find_element_by_link_text("New customers click here").click()

    find_and_fill_element(wd, 'tax_id', "1")
    find_and_fill_element(wd, 'company', "2")
    find_and_fill_element(wd, 'firstname', "3")
    find_and_fill_element(wd, 'lastname', "4")
    find_and_fill_element(wd, 'address1', "5")
    find_and_fill_element(wd, 'address2', "6")
    find_and_fill_element(wd, 'postcode', "123456")
    find_and_fill_element(wd, 'city', "8")
    find_and_fill_element(wd, 'email', mail[0])
    find_and_fill_element(wd, 'phone', "92112345678")
    find_and_fill_element(wd, 'password', "1111")
    find_and_fill_element(wd, 'confirmed_password', "1111")

    ###
    wd.find_element_by_name("create_account").click()

    ###
    wd.find_element_by_link_text("Logout").click()

    find_and_fill_element(wd, 'password', "1111")
    find_and_fill_element(wd, 'email', mail[0])
    wd.find_element_by_name("login").click()
    wd.find_element_by_link_text("Logout").click()

# Задание 13. Сделайте сценарий работы с корзиной
# Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
# Сценарий должен состоять из следующих частей:
# 1) открыть страницу какого-нибудь товара
# 2) добавить его в корзину
# 3) подождать, пока счётчик товаров в корзине обновится
# 4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
# 5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
# 6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
        sleep(1)
        #http: // stackoverflow.com / questions / 18607999 / how - to - wait - and -get - value - of - span - object - in -selenium - python - binding

        #.//*[ @id='cart']//a//span[ @class ='quantity']
        #< spanclass ="quantity" style="" > 1 < / span >
        wait=WebDriverWait(wd,10)
        #подготовим условие ".//*[ @ id = 'cart']//a//span[@class='quantity' and text()!=0")
        #x_path=(".//*[ @ id = 'cart']//a//span[@class='quantity' and text()="+str(i)+"]")
        #print(x_path)
        #element = wait.until(EC.text_to_be_present_in_element(By.XPATH,x_path))
        #element = wait.until(EC.text_to_be_present_in_element(By.XPATH,".//*[ @ id = 'cart']//a//span[@class='quantity' and text()=1]"))
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH,".//*[ @ id = 'cart']//a//span[@class='quantity']"),str(i)))
        #вот тут как раз и ждем что поменяется свойство текст у элемента а потом щелкаем по главной странице
        wd.get("http://localhost/litecart/en/")

    #открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
    wd.get("http://localhost/litecart/en/checkout")
    sleep(10)
    order=wd.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']")
    print("Total_order_distinct_prod:"+str(len(order)))

    for i in range(len(order)): #так как может быть случайно 2 раза один и тотже товар заказан надо искать уникальные
        wd.find_element_by_name('remove_cart_item').click()
        wait = WebDriverWait(wd, 10)
        wait.until(EC.staleness_of(order[0]))
        #если .//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class="unit-cost"] есть то элементы еще остались.
        #sleep(1)


