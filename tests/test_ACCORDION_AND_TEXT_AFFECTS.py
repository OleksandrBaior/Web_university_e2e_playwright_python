# Click on every item and verify if the text appeared
# Wait for the text in the last item

from playwright.sync_api import expect
from pages.accordion_and_text_affects_page import Accordion_and_text_affects
import pytest


class Test_Accordion_and_text_affects:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        # self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.accordion_and_text_affects = Accordion_and_text_affects(self.page)
        page.goto('/Accordion/index.html')

    def test_manual_testing_section(self, test_setup):
        self.accordion_and_text_affects.manual_testing_btn.click()
        self.accordion_and_text_affects.check_manual_testing_text_appear(self.accordion_and_text_affects.manual_testing_accordion, self.accordion_and_text_affects.manual_testing_text)

    def test_accordion_and_text_affects_section(self, test_setup):
        self.accordion_and_text_affects.cucumber_BDD_btn.click()
        self.accordion_and_text_affects.check_manual_testing_text_appear(self.accordion_and_text_affects.cucumber_BDD_accordion, self.accordion_and_text_affects.cucumber_BDD_text)

    def test_automation_testing_section(self, test_setup):
        self.accordion_and_text_affects.automation_testing_btn.click()
        self.accordion_and_text_affects.check_manual_testing_text_appear(self.accordion_and_text_affects.automation_testing_accordion, self.accordion_and_text_affects.automation_text)
    
    @pytest.mark.e2e
    def test_keep_clicking_section(self, test_setup):
        expect(self.accordion_and_text_affects.loading).to_contain_text('LOADING COMPLETE.', timeout=12000)
        self.accordion_and_text_affects.keep_cliking_btn.click()
        self.accordion_and_text_affects.check_manual_testing_text_appear(self.accordion_and_text_affects.keep_cliking_accordion, self.accordion_and_text_affects.keep_cliking_text)
