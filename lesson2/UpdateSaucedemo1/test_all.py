from selenium.webdriver.common.by import By
import time
from locators_1 import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, BUTTON_ADD_TO_CARD,\
    SHOPPING_CART, SHOPPING_CART_LINK, REMOVE_BUTTON, ITEM_CARD, ADD_ITEM, ITEM_IMAGE, ITEM_NAME,\
    FILTER_ICON, FILTER_A_TO_Z, FILTER_TYPE, BURGER_MENU, ABOUT_BUTTON, RESET_APP, CHECKOUT_BUTTON,\
    FIRST_NAME_FIELD, LAST_NAME_FIELD, ZIPCODE_FIELD, CONTINUE_BUTTON, FINISH_BUTTON, LOGOUT_BUTTON
from data_1 import LOGIN, PASSWORD, MAIN_PAGE, INVENTORY_PAGE, WRONG_LOGIN, WRONG_PASSWORD, \
    ITEM_PAGE, ABOUT_PAGE, FIRST_NAME, LAST_NAME, ZIPCODE, CHECKOUT_COMPLETE
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



def test_login_form(driver, sign_in):
    assert driver.current_url == INVENTORY_PAGE



def test_wrong_login(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*USERNAME_FIELD).send_keys(WRONG_LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(WRONG_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    assert driver.current_url == MAIN_PAGE

def test_add_item_to_cart(driver, sign_in):
    driver.find_element(*BUTTON_ADD_TO_CARD).click()
    driver.find_elements(*SHOPPING_CART)
    assert len(SHOPPING_CART) > 0


def test_remove_item_from_cart(driver, sign_in):
    driver.find_element(*BUTTON_ADD_TO_CARD).click()
    driver.find_element(*SHOPPING_CART_LINK).click()
    driver.find_element(*REMOVE_BUTTON).click()
    time.sleep(2)
    driver.find_elements(*SHOPPING_CART)
    assert len(SHOPPING_CART) != 0


def test_add_item_from_item_card(driver, sign_in):
    driver.find_element(*ITEM_CARD).click()
    driver.find_element(*ADD_ITEM).click()
    driver.find_elements(*SHOPPING_CART)
    assert len(SHOPPING_CART) >= 0

def test_image(driver, sign_in):
    driver.find_element(*ITEM_IMAGE).click()
    assert driver.current_url == ITEM_PAGE


def test_item_name(driver, sign_in):
    driver.find_element(*ITEM_NAME).click()
    assert driver.current_url == ITEM_PAGE


def test_about_link(driver, sign_in):
    driver.find_element(*BURGER_MENU).click()
    time.sleep(2)
    driver.find_element(*ABOUT_BUTTON).click()
    assert driver.current_url == ABOUT_PAGE


def test_reset_app(driver, sign_in):
    driver.find_element(*BURGER_MENU).click()
    time.sleep(2)
    driver.find_element(*RESET_APP).click()
    driver.find_elements(*SHOPPING_CART)
    assert len(SHOPPING_CART) != 0


def test_item_checkout(driver, sign_in):
    driver.find_element(*BUTTON_ADD_TO_CARD).click()
    driver.find_element(*SHOPPING_CART_LINK).click()
    driver.find_element(*CHECKOUT_BUTTON).click()
    driver.find_element(*FIRST_NAME_FIELD).send_keys(FIRST_NAME)
    driver.find_element(*LAST_NAME_FIELD).send_keys(LAST_NAME)
    driver.find_element(*ZIPCODE_FIELD).send_keys(ZIPCODE)
    driver.find_element(*CONTINUE_BUTTON).click()
    driver.find_element(*FINISH_BUTTON).click()
    assert driver.current_url == CHECKOUT_COMPLETE

def test_logout(driver, sign_in):
    driver.find_element(*BURGER_MENU).click()
    time.sleep(3)
    driver.find_element(*LOGOUT_BUTTON).click()
    assert driver.current_url == MAIN_PAGE








