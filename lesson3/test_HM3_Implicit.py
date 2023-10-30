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
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_registration_with_implicit(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    assert driver.find_element(By.CSS_SELECTOR, 'body > h1').text == "Практика с ожиданиями в Selenium"

    driver.find_element(By.CSS_SELECTOR, 'button[id="startTest"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input[id="login"] ').send_keys("login")
    driver.find_element(By.CSS_SELECTOR, 'input[id="password"] ').send_keys("password")
    driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[id="register"]').click()

    assert driver.find_element(By.CSS_SELECTOR, 'div[id="loader"]').is_displayed()
    # time.sleep(5)
    assert driver.find_element(By.CSS_SELECTOR, 'p[id="successMessage"]').text ==\
           "Вы успешно зарегистрированы!"
