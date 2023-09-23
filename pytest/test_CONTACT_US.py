from playwright.sync_api import Page, expect
import pytest

BASE_URL = "http://webdriveruniversity.com/Contact-Us/contactus.html"
TITLE = "WebDriver | Contact Us"
FIRST_NAME = "Robie"
SECOND_NAME = "Margo"
EMAIL = "test@gmail.com"
INVALID_EMAIL ="test@gmail"
COMMENT = "My first comment"
THANKS_TEXT = 'Thank You for your Message!'
ERROR_ALL_FIELD_REQUIRED = "Error: all fields are required Error: Invalid email address"
ERROR_INVALID_EMAIL = "Error: Invalid email address"

first_name_fild = '//*[@id="contact_form"]/input[1]'
second_name_field = '//*[@id="contact_form"]/input[2]'
email_field = '//*[@id="contact_form"]/input[3]'
coment_field = '//*[@id="contact_form"]/textarea'
submit_button = '//*[@id="form_buttons"]/input[2]'
thanks_text = '//*[@id="contact_reply"]/h1'
error_all_field_required_text = "//html/body"

# @pytest.mark.skip("chromium")
# @pytest.mark.only_browser("firefox")

def test_verify_submit_comment_with_all_filled_filds(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title(TITLE)

    page.locator(first_name_fild).fill(FIRST_NAME)
    expect(page.locator(first_name_fild)).to_have_value(FIRST_NAME)
    page.locator(second_name_field).fill(SECOND_NAME)
    expect(page.locator(second_name_field)).to_have_value(SECOND_NAME)
    page.locator(email_field).fill(EMAIL)
    expect(page.locator(email_field)).to_have_value(EMAIL)
    page.locator(coment_field).fill(COMMENT)
    expect(page.locator(coment_field)).to_have_value(COMMENT)
    page.locator(submit_button).click()
    expect(page.locator(thanks_text)).to_contain_text(THANKS_TEXT)


def test_verify_submit_comment_with_all_empty_filds(page: Page):
    page.goto(BASE_URL)
    page.locator(submit_button).click()
    expect(page.locator(error_all_field_required_text)).to_contain_text(ERROR_ALL_FIELD_REQUIRED)
   

def test_verify_submit_comment_with_all_with_invalid_email(page: Page):
    page.goto(BASE_URL)
    page.locator(first_name_fild).fill(FIRST_NAME)
    expect(page.locator(first_name_fild)).to_have_value(FIRST_NAME)
    page.locator(second_name_field).fill(SECOND_NAME)
    expect(page.locator(second_name_field)).to_have_value(SECOND_NAME)
    page.locator(email_field).fill(INVALID_EMAIL)
    expect(page.locator(email_field)).to_have_value(INVALID_EMAIL)
    page.locator(coment_field).fill(COMMENT)
    expect(page.locator(coment_field)).to_have_value(COMMENT)
    page.locator(submit_button).click()
    expect(page.locator(error_all_field_required_text)).to_contain_text(ERROR_INVALID_EMAIL)