from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page


    def navigate_to(self, url: str):
        """Navigates to a specific URL."""
        self.page.goto(url)


