from playwright.sync_api import Page, expect

class BasePage:
    """
    Base Page containing reusable UI interactions, explicit waits,
    and assertion wrappers for all Page Objects.
    """
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str):
        self.page.wait_for_selector(selector, state="visible")
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.wait_for_selector(selector, state="visible")
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.page.wait_for_selector(selector, state="visible")
        return self.page.locator(selector).inner_text().strip()

    def is_visible(self, selector: str) -> bool:
        try:
            return self.page.locator(selector).is_visible()
        except Exception:
            return False

    def take_screenshot(self, filepath: str):
        self.page.screenshot(path=filepath, full_page=True)

    def get_title(self) -> str:
        return self.page.title()
