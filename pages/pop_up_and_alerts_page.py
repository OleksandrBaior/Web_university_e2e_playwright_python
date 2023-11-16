from playwright.sync_api import Page, expect

class Pop_up_and_alerts_page:

    def __init__(self, page: Page):
        self.page = page
        
        self.javaScript_alert_btn = page.locator('//*[@id="button1"]')
        self.modal_popup_btn = page.locator('//*[@id="button2"]')
        self.modal_close_btn = page.locator('//*[@id="myModal"]/div/div/div[3]/button')
        self.modal_title = page.locator('//*[@id="myModal"]/div/div/div[1]')
        self.jAjax_loadert_btn = page.locator('//*[@id="button3"]')
        self.click_me_btn = page.locator('//*[@id="button1"]/p')
        self.click_me_modal_title = page.locator('//*[@id="myModalClick"]/div/div/div[1]/h4')
        self.javaScript_confirm_box_btn = page.locator('//*[@id="button4"]')
        self.javaScript_confirm_box_ok = page.locator('//*[@id="confirm-alert-text"]')



      


           