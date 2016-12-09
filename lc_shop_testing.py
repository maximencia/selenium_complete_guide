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