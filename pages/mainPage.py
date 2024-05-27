from .basePage import BasePage
from locators import MainPageLocators
import os
import dotenv

dotenv.load_dotenv()

class MainPage(BasePage):
    def user_login(self, userType):
        input_login = self.browser.find_element(*MainPageLocators.LOGIN)
        input_login.send_keys(userType)
        input_password = self.browser.find_element(*MainPageLocators.PASSWORD)
        input_password.send_keys(os.getenv("PASSWORD"))
        SUBMITBTTN = self.browser.find_element(*MainPageLocators.SUBMITBTTN).click()
        MENUBTTN = self.browser.find_element(*MainPageLocators.MENUBTTN)
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        assert logo.text == "Swag Labs" , "User is non-login"

    def log_out(self):
        self.browser.find_element(*MainPageLocators.MENUBTTN).click()
        self.browser.find_element(*MainPageLocators.LOGOUTBTTN).click()
        login_page_logo = self.browser.find_element(*MainPageLocators.LOGINLOGO)
        assert login_page_logo.text == "Swag Labs" , "User is logged-in"
