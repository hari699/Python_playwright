from playwright.sync_api import expect
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.checkout_page import Checkout

class TestCompleteUserFlow:
    """Test suite for complete e2e flows."""

    def test_successful_login(self, login_page: LoginPage):
        """Test 1: User can successfully login."""
        login_page.navigate_to("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

        expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")


    def test_failed_login(self, login_page: LoginPage):
        """Test 2: Login fails with invalid username."""

        login_page.navigate_to("https://www.saucedemo.com/")
        login_page.login("invalid_user", "secret_sauce")

        # Wait for and verify error message
        login_page.error_message().wait_for(state="visible", timeout=5000)
        expect(login_page.error_message()).to_contain_text("Epic sadface")

    def test_failed_password_login(self, login_page: LoginPage):
        """Test 3: Login fails with invalid password."""
        login_page.navigate_to("https://www.saucedemo.com/")
        login_page.login("standard_user", "secre_12313")

        # Wait for and verify error message
        login_page.error_message().wait_for(state="visible", timeout=5000)
        expect(login_page.error_message()).to_contain_text("Epic sadface")

    def test_add_to_cart(self, authenticated_page: LoginPage, inventory_page):
        """Test 4: Adding an item to cart."""
        # Verify we're on inventory page
        expect(inventory_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

        # Click add to cart button
        inventory_page.add_to_cart().click()


    def test_cart_icon(self, authenticated_page: LoginPage, inventory_page: InventoryPage):
        """Test 5: Adding an item to cart."""
        inventory_page.cart_icon().click()

    def test_check_out(self, authenticated_page: LoginPage, inventory_page: InventoryPage, checkout_page: Checkout):
        """Test 6: Checking out."""
        inventory_page.add_to_cart().click()
        inventory_page.cart_icon().click()

        #click checkout after adding to the cart
        checkout_page.click_checkout().click()
        checkout_page.fill_form("hari", "s", "65456")

        #click the continue button
        checkout_page.click_submit().click()

        checkout_page.click_finish().click()

        #assert order confirmation
        expect(checkout_page.confirmation()).to_contain_text("Thank you for your order!")

        checkout_page.page.screenshot(path="tests/screenshot/orderConfirmation.png")









