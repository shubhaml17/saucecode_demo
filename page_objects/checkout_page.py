from locators.locators import CheckoutPageLocators


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(*CheckoutPageLocators.CHECKOUT_BUTTON).click()

    def enter_user_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*CheckoutPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*CheckoutPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*CheckoutPageLocators.ZIP_CODE_INPUT).send_keys(zip_code)
        self.driver.find_element(*CheckoutPageLocators.CONTINUE_BUTTON).click()

    def verify_total_amount(self, expected_amount):
        total = self.driver.find_element(*CheckoutPageLocators.TOTAL_AMOUNT).text
        return expected_amount in total

    def finish_checkout(self):
        self.driver.find_element(*CheckoutPageLocators.FINISH_BUTTON).click()

    def verify_thank_you(self):
        return self.driver.find_element(*CheckoutPageLocators.THANK_YOU_HEADER).is_displayed()
