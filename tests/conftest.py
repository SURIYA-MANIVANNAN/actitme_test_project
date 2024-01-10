import pytest
from selenium import webdriver

@pytest.fixture()
def initialize_driver():

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    driver= webdriver.Chrome(options=opt)

    """url launching"""
    url = "https://demo.actitime.com/login.do"
    driver.get(url)

    yield driver

    driver.close()



