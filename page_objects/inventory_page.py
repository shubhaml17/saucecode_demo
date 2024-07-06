from locators.locators import InventoryPageLocators


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def sort_products_low_to_high(self):
        sort_dropdown = self.driver.find_element(*InventoryPageLocators.SORT_DROPDOWN)
        sort_dropdown.click()
        sort_dropdown.find_element(*InventoryPageLocators.LOW_TO_HIGH).click()

    def add_lowest_priced_product(self):
        self.driver.find_element(*InventoryPageLocators.ADD_TO_CART_BUTTON).click()

    def go_to_cart(self):
        self.driver.find_element(*InventoryPageLocators.CART_BUTTON).click()
