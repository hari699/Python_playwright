
from Pages.base_page import BasePage

class InventoryPage(BasePage):
    def add_to_cart(self):
        return self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
    def cart_icon(self):
        return self.page.locator("[data-test='shopping-cart-link']")


