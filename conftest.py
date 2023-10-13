from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope = 'function')
def new_page(playwright: Playwright, request):
    browser = playwright.chromium.launch(headless= False)
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    # page.goto('http://webdriveruniversity.com')
    yield page
    browser.close()