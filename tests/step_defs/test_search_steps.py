from pytest_bdd import scenarios, when, then, given, parsers
from selenium.webdriver.common.by import By


# Constants
ADDREMOVEELEMENTS_HOME = 'https://the-internet.herokuapp.com/add_remove_elements/'

# Scenarios
scenarios("../features/addRemoveElements.feature")

# Shared Given Steps
@given('the AddRemoveElements home page is displayed')
def add_home(browser):
    browser.get(ADDREMOVEELEMENTS_HOME)
# When Steps

@when('the user click AddElement button')
def click_add_element_button(browser):
    add_button = browser.find_element(By.CSS_SELECTOR, 'body>div>div>div>button')
    add_button.click()

@then('the Delete button has appear')
def is_delete_button_displayed(browser):
    del_button = browser.find_element(By.CSS_SELECTOR, 'body>div>div>div>div>button')
    del_button.is_displayed()
