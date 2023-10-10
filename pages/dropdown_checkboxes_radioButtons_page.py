from playwright.sync_api import Page, expect

class Dropdown_checkboxes_radioButtons:

    def __init__(self, page: Page):
        self.page = page
        self.drop_down_1 = page.locator('//*[@id="dropdowm-menu-1"]')
        self.drop_down_2 = page.locator('//*[@id="dropdowm-menu-2"]')
        self.drop_down_3 = page.locator('//*[@id="dropdowm-menu-3"]')
        self.dropdown_menu_1 = ['java', 'c#', 'python', 'sql']
        self.dropdown_menu_2 = ['eclipse', 'maven', 'testng', 'junit']
        self.dropdown_menu_3 = ['html', 'css', 'javascript', 'jquery']

        self.checkbox = page.locator('//*[@id="checkboxes"]')
     
        self.radion_buttons = page.locator('//*[@id="radio-buttons"]')
        self.radion_buttons_list = ['green', 'blue', 'yellow', 'orange', 'purple']


        
        
    def select_drop_down_option(self, drop_down_menu, drop_down_locator) -> None:
       for item in drop_down_menu:
           drop_down_locator.select_option(value=item)

    def mark_checkbox(self, checkbox) -> None:
        COUNT_ELEMENTS = checkbox.locator('input').count()
        for i in range(COUNT_ELEMENTS):
           self.page.locator(f'//*[@id="checkboxes"]/label[{i+1}]/input').check()

    def check_all_checkboxes_marked(self, checkbox) -> None:
        COUNT_ELEMENTS = checkbox.locator('input').count()
        for i in range(COUNT_ELEMENTS):
            expect(self.page.locator(f'//*[@id="checkboxes"]/label[{i+1}]/input')).to_be_checked()

    def mark_and_check_radio_button(self, radio_buttons) -> None:
        COUNT_ELEMENTS = radio_buttons.locator('input').count()
        for i in range(COUNT_ELEMENTS):
            self.page.locator(f'//*[@id="radio-buttons"]/input[{i+1}]').check()

            for y in range(COUNT_ELEMENTS):
                if i+1 == y+1:
                    expect(self.page.locator(f'//*[@id="radio-buttons"]/input[{y+1}]')).to_be_checked()
                else:
                    expect(self.page.locator(f'//*[@id="radio-buttons"]/input[{y+1}]')).not_to_be_checked()
            