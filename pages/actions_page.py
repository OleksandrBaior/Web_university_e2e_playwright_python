from playwright.sync_api import Page, expect

class Actions:

    def __init__(self, page: Page):
        self.page = page
        self.drop_section = page.locator('//*[@id="droppable"]')
        self.drop_section_after_drop = page.locator('//*[@id="droppable"]/p')
        self.drag_item = page.locator('//*[@id="draggable"]')

        self.double_click_section = page.locator('//*[@id="double-click"]')

        self.hover_first = page.locator('//*[@id="div-hover"]/div[1]/button')
        self.link_1_hover = page.locator('//*[@id="div-hover"]/div[1]/div/a')

        self.hover_second = page.locator('//*[@id="div-hover"]/div[2]/button')
        self.link_2_hover = page.locator('//*[@id="div-hover"]/div[2]/div/a')

        self.hover_third = page.locator('//*[@id="div-hover"]/div[3]/button')
        self.link_3_hover_1 = page.locator('//*[@id="div-hover"]/div[3]/div/a[1]')
        self.link_3_hover_2 = page.locator('//*[@id="div-hover"]/div[3]/div/a[2]')

        self.click_and_hold_btn = page.locator('//*[@id="click-box"]')

    def check_element_visible (self, elem_1, elem_2) -> None:
        expect(elem_1).to_be_visible()
        if elem_2 != None:
            expect(elem_2).to_be_visible()
        elem_1.click()
        self.page.on("dialog", lambda dialog: dialog.accept())

    def click_and_hold_element(self, element):
        element_box = element.bounding_box()
        if element_box:
            x_center = element_box['x'] + element_box['width'] / 2
            y_center = element_box['y'] + element_box['height'] / 2
            self.page.mouse.move(x_center, y_center)
            self.page.mouse.down()
    


            
        
        

