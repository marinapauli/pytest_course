from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_item_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    button_add_to_cart = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    button_add_to_cart.click()
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
    cart.click()
    time.sleep(2)

    shopping_cart_after = driver.find_elements(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert len(shopping_cart_after) > 0


def test_remove_item_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button_add_to_cart.click()
    time.sleep(3)

    cart = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
    cart.click()
    time.sleep(2)

    remove_button = driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    remove_button.click()

    shopping_cart_after = driver.find_elements(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert len(shopping_cart_after) == 0


def test_add_item_from_item_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(2)

    item_card = driver.find_element(By.CSS_SELECTOR, 'a#item_4_title_link')
    item_card.click()
    time.sleep(2)

    add_to_cart = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
    add_to_cart.click()

    shopping_cart_after = driver.find_elements(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert len(shopping_cart_after) > 0






