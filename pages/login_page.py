from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver=driver
        self.username_input = (By.XPATH, "//input[@data-qa='login-email']")
        self.password_input = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_button = (By.XPATH, "//button[text()='Login']")
        self.invalid_login_message = (By.XPATH, "//p[text()='Your email or password is incorrect!']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

        
