import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.home_page import HomePage
from test_data.user_data import TestData

user_data = TestData().get_user_data("valid_user")

def test_valid_user_login(driver: WebDriver):
    # Arrange
    driver.get("https://automationexercise.com/login")
    login_page = LoginPage(driver)

    # Act
    login_page.enter_username(user_data["Email"])
    login_page.enter_password(user_data["Password"])
    login_page.click_login()

    # Assert
    home_page = HomePage(driver)
    assert "Automation Exercise" in home_page.get_title()

invalid_user_data= TestData().get_user_data("invalid_user")

def test_invalid_user_login(driver: WebDriver):
    # Arrange
    driver.get("https://automationexercise.com/login")
    login_page = LoginPage(driver)

    # Act
    login_page.enter_username(invalid_user_data["Email"])
    login_page.enter_password(invalid_user_data["Password"])
    login_page.click_login()

    # Assert
    error_message = driver.find_element(*login_page.invalid_login_message)
    assert "Your email or password is incorrect!" in error_message.text

empty_user_data = TestData().get_user_data("empty_user")

def test_empty_user_login(driver: WebDriver):
    # Arrange
    driver.get("https://automationexercise.com/login")
    login_page = LoginPage(driver)

    # Act
    login_page.enter_username(empty_user_data["Email"])
    login_page.enter_password(empty_user_data["Password"])
    login_page.click_login()

    # Assert
    email_input = driver.find_element(*login_page.username_input)
    validation_message = email_input.get_attribute("validationMessage")
    assert "Please fill in this field." in validation_message


