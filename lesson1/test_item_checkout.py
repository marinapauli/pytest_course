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

    checkout_button = driver.find_element(By.CSS_SELECTOR, 'button.checkout_button')
    checkout_button.click()

    first_name_field = driver.find_element(By.XPATH, '//input[@data-test="firstName"]')
    first_name_field.send_keys("Julie")

    last_name_field = driver.find_element(By.XPATH, '//input[@data-test="lastName"]')
    last_name_field.send_keys("Smith")

    zip_code_field = driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    zip_code_field.send_keys("90555")

    button_continue = driver.find_element(By.XPATH, '//input[@data-test="continue"]')
    button_continue.click()

    button_finish = driver.find_element(By.CSS_SELECTOR, 'button[id = "finish"] ')
    button_finish.click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
