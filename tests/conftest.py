import pytest
from playwright.sync_api import sync_playwright
from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Pages.checkout_page import Checkout


@pytest.fixture
def login_page(page):
    """Initialize LoginPage with the page from pytest-playwright."""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    """Initialize InventoryPage with the page from pytest-playwright."""
    return InventoryPage(page)


@pytest.fixture
def checkout_page(page):
    """Initialize Checkout page with the page from pytest-playwright."""
    return Checkout(page)


@pytest.fixture
def authenticated_page(login_page):
    """
    Fixture that logs in the user and returns authenticated LoginPage.
    Use this when you need a user already logged in.
    """
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    return login_page