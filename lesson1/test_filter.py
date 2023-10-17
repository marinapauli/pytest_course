from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def test_filter_AtoZ_check():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    filter_button = driver.find_element(By.CSS_SELECTOR, 'select[class ="product_sort_container"]')
    filter_button.click()

    filter_icon = driver.find_element(By.CSS_SELECTOR, 'span.select_container')
    filter_icon.click()
    filter_choice = driver.find_element(By.CSS_SELECTOR, 'div > span > select > option:nth-child(1)')
    filter_choice.click()

    filter_type = driver.find_element(By.CSS_SELECTOR, '#header_container span >span ')
    assert filter_type.text == 'Name (A to Z)'


def test_filter_LowToHigh_check():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    filter_button = driver.find_element(By.CSS_SELECTOR, 'select[class ="product_sort_container"]')
    filter_button.click()

    filter_icon = driver.find_element(By.CSS_SELECTOR, 'span.select_container')
    filter_icon.click()
    filter_choice = driver.find_element(By.CSS_SELECTOR,'div > span > select > option:nth-child(3)')
    filter_choice.click()

    filter_type = driver.find_element(By.CSS_SELECTOR,'#header_container span >span ')
    assert filter_type.text == 'Price (low to high)'


