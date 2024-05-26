from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMITBTTN = (By.ID, "login-button")
    MENUBTTN = (By.ID, "react-burger-menu-btn")
    LOGOUTBTTN = (By.ID, "logout_sidebar_link")
    LOGINLOGO = (By.CLASS_NAME, "login_logo")
    LOGO = (By.CLASS_NAME, "app_logo")
