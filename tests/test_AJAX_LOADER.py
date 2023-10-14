# Wait for button and click it

from playwright.sync_api import expect, Page
import pytest

CLICK_ME_BUTTON = '//*[@id="button1"]/p'

class Test_Ajax_Loader:

    @pytest.fixture
    def test_setup(self, new_page, page: Page) -> None:
        page.goto('/Ajax-Loader/index.html')


    @pytest.mark.ajax
    def test_wait_ajax_loader(self, test_setup, page: Page) -> None:
        
        page.locator(CLICK_ME_BUTTON).wait_for(state="visible")
        page.locator(CLICK_ME_BUTTON).click()
        
        
