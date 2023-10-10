# Try to iterate with all items

from playwright.sync_api import expect
from pages.dropdown_checkboxes_radioButtons_page import Dropdown_checkboxes_radioButtons
import pytest


class test_DROPDOWN_CHECKBOX_AND_RADIO_BUTTON:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        page.goto('/Dropdown-Checkboxes-RadioButtons/index.html')
        self.dropdown_checkboxes_radioButtons = Dropdown_checkboxes_radioButtons(self.page)
    
    @pytest.mark.menu
    def test_dropdown_menu(self, test_setup): 
        self.dropdown_checkboxes_radioButtons.select_drop_down_option(self.dropdown_checkboxes_radioButtons.dropdown_menu_1, self.dropdown_checkboxes_radioButtons.drop_down_1)
        self.dropdown_checkboxes_radioButtons.select_drop_down_option(self.dropdown_checkboxes_radioButtons.dropdown_menu_2, self.dropdown_checkboxes_radioButtons.drop_down_2)
        self.dropdown_checkboxes_radioButtons.select_drop_down_option(self.dropdown_checkboxes_radioButtons.dropdown_menu_3, self.dropdown_checkboxes_radioButtons.drop_down_3)
    
    @pytest.mark.menu
    def test_checkbox(self, test_setup):
        self.dropdown_checkboxes_radioButtons.mark_checkbox(self.dropdown_checkboxes_radioButtons.checkbox)
        self.dropdown_checkboxes_radioButtons.check_all_checkboxes_marked(self.dropdown_checkboxes_radioButtons.checkbox)

    @pytest.mark.test
    def test_radio_buttons(self, test_setup):
        self.page.pause()
        self.dropdown_checkboxes_radioButtons.mark_and_check_radio_button(self.dropdown_checkboxes_radioButtons.radion_buttons)
        
    