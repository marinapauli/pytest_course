from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test_registration_explicit(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    assert driver.find_element(By.CSS_SELECTOR, 'body > h1 ').text ==\
           'Практика с ожиданиями в Selenium'

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="startTest"]'))).click()
    driver.find_element(By.CSS_SELECTOR, 'input[id="login"] ').send_keys("login")
    driver.find_element(By.CSS_SELECTOR, 'input[id="password"] ').send_keys("password")
    driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
    driver.find_element(By.CSS_SELECTOR, 'button[id="register"]').click()

    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="loader"]'))).is_displayed()
    # time.sleep(5)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[id="loader"]')))
    assert driver.find_element(By.CSS_SELECTOR, 'p[id="successMessage"]').text == \
           "Вы успешно зарегистрированы!"
