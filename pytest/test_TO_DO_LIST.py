import pytest
from playwright.sync_api import Page, expect

TODO_ITEM = '//*[@id="container"]/ul/li[1]/span/i'
LIST_TODO = 'div ul'
INPUT_FIELD = '//*[@id="container"]/input'

# @pytest.mark.smoke
def test_verify_add_delete_todos(page: Page):
    page.goto('/To-Do-List/index.html')
    
# Delete all todos
    COUNT_ELEMENTS = page.locator(LIST_TODO).locator('li').count()
    while COUNT_ELEMENTS  > 0:
            page.locator(TODO_ITEM).click()
            COUNT_ELEMENTS -= 1
            expect(page.locator(LIST_TODO).locator('li')).to_have_count(COUNT_ELEMENTS)
    
# Add 3 todos
    for item in range(3):
        page.locator(INPUT_FIELD).fill(f'todo {item + 1}')
        page.keyboard.press("Enter")
        expect(page.locator(f'//*[@id="container"]/ul/li[{item + 1}]')).to_contain_text(f'todo {item + 1}')

# Delete 3rd todo 
# Delete 2nd todo 
# Delete last one

    COUNT_TODOS = page.locator(LIST_TODO).locator('li').count()
    for item in reversed(range(COUNT_TODOS)):
        page.locator(f'//*[@id="container"]/ul/li[{item + 1}]/span/i').click()
        COUNT_TODOS -= 1
        expect(page.locator(LIST_TODO).locator('li')).to_have_count(COUNT_TODOS)
     
     
      




  