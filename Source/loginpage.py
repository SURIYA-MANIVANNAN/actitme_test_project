import time
from Generic.excel_lib import readlocators

loc_filepath = r"C:\Users\SURI\PycharmProjects\testingproject1\files\actitime_locators.xlsx"
login_sheet_name = "login_objects"


class Login_page:
    locators = readlocators(loc_filepath,login_sheet_name)

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        """ entering username in username textfield """
        self.driver.findelement(*self.locators["username_txt"]).sendkeys(username)
        time.sleep(3)

    def enter_passworc(self,password):
        """entering password in password textfield"""
        self.driver.findelemet(*self.locators["password_txt"]).sendkeys(password)
        time.sleep(3)

    def click_login(self):
        """click on login button"""
        self.driver.findelement(*self.locators["login_btn"]).click()
        time.sleep(3)






