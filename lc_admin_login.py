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



def test_admin_login(wd):
    wd.get("http://localhost/litecart/admin/login.php")
    wd.implicitly_wait(60)
    find_and_fill_element(wd,element_name="username",value="admin")
    find_and_fill_element(wd,element_name="password",value="admin")
    wd.find_element_by_name("login").click()
    sleep(5)

