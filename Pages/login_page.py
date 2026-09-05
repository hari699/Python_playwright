from Pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, username, password):
        self.user_input().fill(username)
        self.user_password_input().fill(password)
        self.login_btn().click()

    def user_input(self):
        return self.page.get_by_placeholder("Username")

    def user_password_input(self):
        return self.page.get_by_placeholder("Password")

    def login_btn(self):
        return self.page.get_by_role("button", name="login")

    def error_message(self):
        return self.page.locator("[data-test='error']")



