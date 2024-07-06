from locators.locators import LoginPageLocators
from page_objects.login_page import LoginPage
import pytest


@pytest.mark.parametrize("username,password,expected_url,expected_element", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html", LoginPageLocators.APP_LOGO),
    ("locked_out_user", "secret_sauce", "https://www.saucedemo.com/", LoginPageLocators.ERROR_MESSAGE)
])
def test_login(browser, username, password, expected_url, expected_element):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login(username, password)
    browser.implicitly_wait(10)

    try:
        assert browser.current_url == expected_url

        if expected_element == LoginPageLocators.APP_LOGO:
            assert login_page.is_app_logo_displayed()
        elif expected_element == LoginPageLocators.ERROR_MESSAGE:
            error_message = login_page.get_error_message()
            assert "Epic sadface: Sorry, this user has been locked out." in error_message

    except AssertionError as e:
        screenshot_path = f"C:\\Users\\DELL\\PycharmProjects\\demoProject\\screenshot\\screenshot_{username}.png"
        browser.save_screenshot(screenshot_path)
        raise AssertionError(f"{str(e)}. Screenshot saved to {screenshot_path}")
