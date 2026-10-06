import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import Config

@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(page):
    """
    Smoke Test: Verify standard user can successfully log in
    and reach the product dashboard.
    """
    login_page = LoginPage(page).open()
    login_page.login(Config.STANDARD_USER, Config.DEMO_PASSWORD)

    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded(), "Dashboard failed to load after valid login"
    assert "inventory.html" in page.url, "URL did not navigate to inventory page"

@pytest.mark.ui
@pytest.mark.regression
def test_locked_out_user_shows_error(page):
    """
    Regression Negative Test: Verify locked out user receives an error banner.
    """
    login_page = LoginPage(page).open()
    login_page.login(Config.LOCKED_OUT_USER, Config.DEMO_PASSWORD)

    assert login_page.is_error_displayed(), "Error banner was expected but not displayed"
    assert "locked out" in login_page.get_error_message().lower(), (
        f"Unexpected error text: {login_page.get_error_message()}"
    )

@pytest.mark.ui
@pytest.mark.smoke
def test_add_product_to_cart_e2e(page):
    """
    End-to-End Test: Login, add a product to cart, verify badge updates to '1'.
    """
    login_page = LoginPage(page).open()
    login_page.login(Config.STANDARD_USER, Config.DEMO_PASSWORD)

    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded()

    # Initial cart count should be 0
    assert inventory_page.get_cart_count() == "0"

    # Add item
    inventory_page.add_first_product_to_cart()

    # Verify badge displays 1
    assert inventory_page.get_cart_count() == "1", "Cart badge did not increment to 1"
