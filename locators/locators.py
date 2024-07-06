from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    APP_LOGO = (By.CLASS_NAME, 'app_logo')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message-container')


class InventoryPageLocators:
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    ADD_TO_CART_BUTTON = (By.NAME, 'add-to-cart-sauce-labs-onesie')
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    LOW_TO_HIGH = (By.XPATH, "//option[@value='lohi']")


class CheckoutPageLocators:
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_CODE_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')
    TOTAL_AMOUNT = (By.CLASS_NAME, 'summary_total_label')
    THANK_YOU_HEADER = (By.CLASS_NAME, 'complete-header')
