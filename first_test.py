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

def t123(wd):
    wd.find_element_by_name("q").send_keys("nightly")


def test_example(wd):
    wd.get("http://www.google.com/")
    wd.implicitly_wait(60)
    #wd.find_element_by_name("q").send_keys("nightly")
    t123(wd);
    wd.find_element_by_name("btnG").click()
    sleep(10)