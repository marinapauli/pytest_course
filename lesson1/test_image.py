from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_image():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_image = driver.find_element(By.CSS_SELECTOR, 'img[alt="Sauce Labs Backpack"]')
    item_image.click()
    time.sleep(3)

    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4'


def test_item_name():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_name = driver.find_element(By.CSS_SELECTOR, 'a#item_4_title_link')
    item_name.click()
    time.sleep(3)

    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"

