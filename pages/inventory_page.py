from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object for the Products / Inventory Screen."""

    # Locators
    TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    ADD_TO_CART_FIRST_ITEM = "button[id^='add-to-cart']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"

    def is_loaded(self) -> bool:
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Products"

    def add_first_product_to_cart(self):
        self.click(self.ADD_TO_CART_FIRST_ITEM)

    def get_cart_count(self) -> str:
        if self.is_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"

    def open_cart(self):
        self.click(self.CART_LINK)
