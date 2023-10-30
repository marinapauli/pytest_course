from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


import requests
import urllib3
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL

iBrokenImageCount = 0


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


def test_element_creation(driver, wait):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                        'button[class="added-manually"]')))



def test_broken_images(driver, wait):
    driver.get('https://the-internet.herokuapp.com/broken_images')
    image_list = driver.find_elements(By.TAG_NAME, 'img')
    print('Total number of images is ' + str(len(image_list)))

    for img in image_list:
        try:
            response = requests.get(img.get_attribute('src'), stream = True)
            if (response.status_code != 200):
                print(img.get_attribute('outerHTML') + ' is broken.')
                iBrokenImageCount = (iBrokenImageCount + 1)

        except requests.exceptions.MissingSchema:
            print('Encountered MissingSchema Exception')
        except requests.exceptions.InvalidSchema:
            print('Encountered InvalidSchema Exception')
        except:
            print('Encountered some other exception')
print('The page has' + str (iBrokenImageCount) + ' broken images')



def test_check_boxes(driver, wait):
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)').click()
    # driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)').click()
    assert driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)').\
        is_selected()

def test_basic_authorisation(driver):
    driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')


def test_add_box(driver, wait):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    driver.find_element(By.CSS_SELECTOR, 'input[id="adder"] ').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id="box0"]')))

    driver.find_element(By.CSS_SELECTOR, 'input[id="reveal"] ').click()
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="revealed"] ')))


def test_dynamic_properties(driver, wait):
    driver.get('https://demoqa.com/dynamic-properties')
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[id="colorChange"]')))

def test_dynamic_loading1(driver,wait):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
    assert wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#finish > h4')))


def test_dynamic_loading2(driver, wait):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.CSS_SELECTOR, '#start > button').click()
    assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#finish > h4')))





