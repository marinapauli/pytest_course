from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def test_login_form():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()


def test_wrong_login():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    error_message = driver.find_element(By.XPATH, '//div[@class = "error-message-container error"]')
    assert driver.current_url == "https://www.saucedemo.com/"











