import pytest

@pytest.fixture()
def new_page(page):
    page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
    yield page
    