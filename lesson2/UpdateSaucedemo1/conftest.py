import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from data_1 import LOGIN, PASSWORD, MAIN_PAGE, INVENTORY_PAGE, WRONG_LOGIN, WRONG_PASSWORD
from locators_1 import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def sign_in(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()




