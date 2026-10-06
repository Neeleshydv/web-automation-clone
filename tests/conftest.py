import pytest
import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from config.config import Config
from api.api_client import ApiClient

@pytest.fixture(scope="session")
def playwright_instance():
    """Session-wide Playwright engine lifecycle fixture."""
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="function")
def browser(playwright_instance):
    """Launches browser instance according to environment configuration."""
    browser_type = getattr(playwright_instance, Config.BROWSER)
    browser = browser_type.launch(
        headless=Config.HEADLESS,
        slow_mo=100 if not Config.HEADLESS else 0
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser, request):
    """Provides an isolated browser context and page per test scenario."""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir="reports/videos/" if not Config.HEADLESS else None
    )
    page = context.new_page()
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)

    # Attach page instance to the test node for screenshot hook
    request.node.page = page

    yield page

    context.close()

@pytest.fixture(scope="function")
def api_client():
    """Provides an initialized API Client session for API testing."""
    client = ApiClient()
    return client

# --- Pytest HTML Reporting Hooks ---

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures screenshots on test failure and embeds directly
    into the pytest-html report.
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        page = getattr(item, "page", None)
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.nodeid.replace("::", "_").replace(".py", "")
            screenshot_path = f"reports/screenshots/{test_name}_{timestamp}.png"
            try:
                page.screenshot(path=screenshot_path)
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html is not None:
                    # Embed screenshot in HTML report
                    extras.append(pytest_html.extras.image(screenshot_path))
            except Exception as e:
                print(f"Failed to capture failure screenshot: {e}")
        report.extras = extras

def pytest_html_report_title(report):
    report.title = "LightX Test Automation Suite - Test Execution Report"

def pytest_configure(config):
    """Add custom environment metadata to the report header."""
    config._metadata = {
        "Project": "LightX Test Automation Suite",
        "Framework": "Playwright + PyTest + Page Object Model",
        "Base URL": Config.BASE_URL,
        "API URL": Config.API_BASE_URL,
        "Browser": Config.BROWSER,
        "Headless": str(Config.HEADLESS)
    }

