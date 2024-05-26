import pytest
from pytest_bdd import given, scenarios, parsers
from pages.mainPage import MainPage
from pages.basePage import BasePage
from selenium.webdriver.common.by import By

scenarios("../features/login.feature")

@pytest.fixture
@given(parsers.parse("I am logged in as {userType} user"))
def test_user_login(browser, userType):
    page = MainPage(browser)
    page.open()
    page.user_login(userType)
    page.log_out()
