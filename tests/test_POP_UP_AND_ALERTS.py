# Try to iterate with all items

from playwright.sync_api import expect
from pages.pop_up_and_alerts_page import Pop_up_and_alerts_page
import pytest


class test_POP_UP_AND_ALERTS:

    @pytest.fixture
    def test_setup(self, new_page) -> None:
        self.page = new_page
        self.page.goto('/Popup-Alerts/index.html')
        self.pop_up_and_alerts_page = Pop_up_and_alerts_page(self.page)
        
    @pytest.mark.alerts
    def test_JavaScript_Alert(self, test_setup) -> None:
        self.pop_up_and_alerts_page.javaScript_alert_btn.click()
        self.page.on("dialog", lambda dialog: dialog.accept())

        self.pop_up_and_alerts_page.modal_popup_btn.click()
        expect(self.pop_up_and_alerts_page.modal_title).to_contain_text("that Easy!!  Well I think it is.....")
        self.pop_up_and_alerts_page.modal_close_btn.click()

        self.pop_up_and_alerts_page.jAjax_loadert_btn.click()

        self.pop_up_and_alerts_page.click_me_btn.wait_for(state="visible")
        expect(self.pop_up_and_alerts_page.click_me_btn).to_contain_text('CLICK ME!')
        self.pop_up_and_alerts_page.click_me_btn.click()
        expect(self.pop_up_and_alerts_page.click_me_modal_title).to_contain_text("Well Done For Waiting....!!!")

        self.page.go_back()
        self.pop_up_and_alerts_page.javaScript_confirm_box_btn.click()
        self.page.on("dialog", lambda dialog: dialog.accept())
        expect(self.pop_up_and_alerts_page.javaScript_confirm_box_ok).to_contain_text("You pressed OK!")




  