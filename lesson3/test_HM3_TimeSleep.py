import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def test_registration(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    header_name = driver.find_element(By.CSS_SELECTOR, 'body > h1 ')
    assert header_name.text == 'Практика с ожиданиями в Selenium'
    time.sleep(6)

    begin_button = driver.find_element(By.CSS_SELECTOR, 'button[id="startTest"]')
    begin_button.click()
    time.sleep(3)

    login = driver.find_element(By.CSS_SELECTOR, 'input[id="login"] ')
    login.send_keys("login")
    password = driver.find_element(By.CSS_SELECTOR, 'input[id="password"] ')
    password.send_keys("password")
    agree_to_rules = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    agree_to_rules.click()
    button_register = driver.find_element(By.CSS_SELECTOR, 'button[id="register"]')
    button_register.click()

    loading_sign = driver.find_element(By.CSS_SELECTOR, 'div[id="loader"]')
    time.sleep(5)
    loading_sign.is_displayed()

    final_message = driver.find_element(By.CSS_SELECTOR, 'p[id="successMessage"]')
    assert final_message.text == "Вы успешно зарегистрированы!"






