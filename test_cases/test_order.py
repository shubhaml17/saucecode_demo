from page_objects.inventory_page import InventoryPage
from page_objects.checkout_page import CheckoutPage


def test_order_product(browser, login_and_navigate_to_inventory):
    inventory_page = InventoryPage(browser)
    inventory_page.sort_products_low_to_high()
    inventory_page.add_lowest_priced_product()
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(browser)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_user_info("John", "Doe", "123")
    assert checkout_page.verify_total_amount("$8.63")
    checkout_page.finish_checkout()
    assert checkout_page.verify_thank_you()
