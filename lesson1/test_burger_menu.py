
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def test_about_link():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.CSS_SELECTOR, 'button[id="react-burger-menu-btn"]')
    burger_menu.click()
    time.sleep(3)
    about_button = driver.find_element(By.CSS_SELECTOR, 'a[id= "about_sidebar_link"]')
    about_button.click()

    assert driver.current_url == 'https://saucelabs.com/'


def test_reset_app():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.CSS_SELECTOR, 'button[id="react-burger-menu-btn"]')
    burger_menu.click()
    time.sleep(3)

    reset_app = driver.find_element(By.CSS_SELECTOR, 'a[id = "reset_sidebar_link"]')
    reset_app.click()

    cart = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
    cart.click()
    shopping_cart_after = driver.find_elements(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert len(shopping_cart_after) == 0
