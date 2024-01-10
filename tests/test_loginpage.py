import pytest
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Source.loginpage import Login_page


data = [("admin","manager"),("admin","traine"),("trainee","trainee")]

@pytest.mark.parametrize('username','password', data)
def test_loginpage(initialize_driver,username, password):
    driver=initialize_driver
    try:
        lp = Login_page(driver)
        lp.enter_username(username)
        lp.enter_passworc(password)
        lp.click_login()

        wait_ = WebDriverWait(15)
        wait_.until(EC.title_is("actiTIME - Enter Time-Track"))

    except Exception as error_msg:
        # get screenshot
        td = datetime.now()
        s_path = r"C:\Users\SURI\PycharmProjects\testingproject1\screenshots"
        name = f"{__name__}-{td.day}-{td.month}-{td.year}-{td.minute}-{td.second}"
        driver.save_screenshot(s_path + name)
        raise error_msg


