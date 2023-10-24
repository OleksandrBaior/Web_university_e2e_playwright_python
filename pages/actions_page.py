from playwright.sync_api import Page 

class Actions:

    def __init__(self, page: Page):
        self.page = page
        self.drop_section = page.locator('//*[@id="droppable"]')
        self.drop_section_after_drop = page.locator('//*[@id="droppable"]/p')
        self.drag_item = page.locator('//*[@id="draggable"]')

        self.double_click_section = page.locator('//*[@id="double-click"]')

        self.hover_first = page.locator('//*[@id="div-hover"]/div[1]/button')
        self.link_1_hover_first = page.locator('//*[@id="div-hover"]/div[1]/div/a')