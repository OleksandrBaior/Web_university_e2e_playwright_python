       
from playwright.sync_api import Page, expect
import pytest

CLICK_ME_BUTTON = '//*[@id="button1"]/p'

class Test_Ajax_Loader:
    @pytest.fixture
    def test_setup(self, new_page: Page) -> None:
        self.page = new_page
        self.page.goto('/Ajax-Loader/index.html')

    @pytest.mark.ajax
    def test_wait_ajax_loader(self, test_setup) -> None:
        self.page.locator(CLICK_ME_BUTTON).wait_for(state="visible")
        self.page.locator(CLICK_ME_BUTTON).click()
        expect(self.page.locator(CLICK_ME_BUTTON)).to_contain_text('CLICK ME!')
