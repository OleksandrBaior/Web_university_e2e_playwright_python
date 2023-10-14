import pytest
from playwright.sync_api import Page

@pytest.fixture()
def new_page(page: Page) -> None:
    page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
    yield page
    