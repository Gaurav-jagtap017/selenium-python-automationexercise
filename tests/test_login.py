import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_valid_user_login(driver: WebDriver):
    # Arrange
    driver.get("https://automationexercise.com/login")
    login_page = LoginPage(driver)

    # Act
    login_page.enter_username("jagtapg017@gmail.com")
    login_page.enter_password("Jagtapg@017")
    login_page.click_login()

    # Assert
    home_page = HomePage(driver)
    assert "Automation Exercise" in home_page.get_title()
