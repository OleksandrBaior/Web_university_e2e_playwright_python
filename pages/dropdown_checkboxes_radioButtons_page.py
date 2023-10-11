from playwright.sync_api import Page, expect

class Dropdown_checkboxes_radioButtons:

    def __init__(self, page: Page):
        self.page = page

        # Dropdown Menu(s)
        self.drop_down_1 = page.locator('//*[@id="dropdowm-menu-1"]')
        self.drop_down_2 = page.locator('//*[@id="dropdowm-menu-2"]')
        self.drop_down_3 = page.locator('//*[@id="dropdowm-menu-3"]')
        self.dropdown_menu_1 = ['java', 'c#', 'python', 'sql']
        self.dropdown_menu_2 = ['eclipse', 'maven', 'testng', 'junit']
        self.dropdown_menu_3 = ['html', 'css', 'javascript', 'jquery']

        # Checkboxe(s)
        self.checkbox = page.locator('//*[@id="checkboxes"]')

        # Radio Button(s)
        self.radion_buttons = page.locator('//*[@id="radio-buttons"]')
        self.radion_buttons_list = ['green', 'blue', 'yellow', 'orange', 'purple']
        
        # Selected & Disabled
        self.selected_disabled_radio_buttons = page.locator('//*[@id="radio-buttons-selected-disabled"]')
        self.disabled_radio_button_element = page.locator('//*[@id="radio-buttons-selected-disabled"]/input[2]')
        self.selected_disabled_drop_down = page.locator('//*[@id="fruit-selects"]')
        self.selected_disabled_drop_down_list = page.query_selector_all('//*[@id="fruit-selects"]/option')
        self.disabled_drop_down_element = page.locator('//*[@id="fruit-selects"]/option[2]')
        
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
    

    def mark_selected_disabled_radio_buttons(self, checkbox) -> None:
        COUNT_ELEMENTS = checkbox.locator('input').count()
        for i in range(COUNT_ELEMENTS):
           if self.page.locator(f'//*[@id="radio-buttons-selected-disabled"]/input[{i+1}]').is_disabled() == False :
                self.page.locator(f'//*[@id="radio-buttons-selected-disabled"]/input[{i+1}]').check()


        
    def selected_disabled_drop_down_option(self, drop_down_menu) -> None:
        for item in drop_down_menu:
            NAME = item.get_attribute('value')
            if item.is_disabled() == False:
                self.selected_disabled_drop_down.select_option(value=NAME)

           