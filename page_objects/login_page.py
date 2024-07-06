from locators.locators import LoginPageLocators


class LoginPage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def is_app_logo_displayed(self):
        return self.driver.find_element(*LoginPageLocators.APP_LOGO).is_displayed()

    def get_error_message(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE).text
