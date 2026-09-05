from Pages.base_page import BasePage

class Checkout(BasePage):
    def click_checkout(self):
        return self.page.get_by_role("button", name="Checkout")

    def fill_form(self, name, lastname, zipcode):
        self.fill_name().fill(name)
        self.fill_lastname().fill(lastname)
        self.fill_zipcode().fill(zipcode)

    def fill_name(self):
        return self.page.get_by_placeholder("First Name")

    def fill_lastname(self):
        return self.page.get_by_placeholder("Last Name")

    def fill_zipcode(self):
        return self.page.get_by_placeholder("Zip/Postal Code")

    def click_submit(self):
        return self.page.get_by_role("button", name="continue")

    def click_finish(self):
        return self.page.get_by_role("button", name="Finish")

    def confirmation(self):
        return self.page.locator('[data-test="complete-header"]')


