# Try to iterate with all items

from playwright.sync_api import expect
from pages.actions_page import Actions
import pytest

class Test_Actions:

    @pytest.fixture
    def test_setup(self, new_page) -> None:
        self.page = new_page
        self.page.goto('/Actions/index.html')
        self.actions = Actions(self.page)

    @pytest.mark.actions
    def test_drag_and_drop(self, test_setup) -> None:
        expect(self.actions.drop_section).to_contain_text('DROP HERE!')
        expect(self.actions.drop_section).to_have_css('background-color', 'rgb(97, 109, 179)')
        self.actions.drag_item.drag_to(self.actions.drop_section)
        expect(self.actions.drop_section).to_contain_text('Dropped!')
        expect(self.actions.drop_section_after_drop).to_have_attribute('style', 'background-color: rgb(244, 89, 80); height: 100%;')

    @pytest.mark.actions
    def test_duble_click(self, test_setup) -> None:
        expect(self.actions.double_click_section).to_have_css('background-color', 'rgb(254, 196, 45)')
        self.actions.double_click_section.dblclick()
        expect(self.actions.double_click_section).to_have_css('background-color', 'rgb(147, 203, 90)')

    @pytest.mark.actions
    def test_hover_three_section(self, test_setup) -> None:
        self.actions.hover_first.hover()
        self.actions.check_element_visible(self.actions.link_1_hover, None)

        self.actions.hover_second.hover()
        self.actions.check_element_visible(self.actions.link_2_hover, None)

        self.actions.hover_third.hover()
        self.actions.check_element_visible(self.actions.link_3_hover_1, self.actions.link_3_hover_2)

    @pytest.mark.actions
    def test_click_and_hold_section(self, test_setup) -> None:
        self.page.pause()
        expect(self.actions.click_and_hold_btn).to_contain_text('Click and Hold!')
        self.actions.click_and_hold_element(self.actions.click_and_hold_btn)
        expect(self.actions.click_and_hold_btn).to_contain_text('Well done! keep holding that click now.....')
        self.page.mouse.up()
        expect(self.actions.click_and_hold_btn).to_contain_text('Dont release me!!!')