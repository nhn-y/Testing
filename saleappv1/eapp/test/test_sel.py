import time

from eapp.test.test_base import driver
from selenium.webdriver.common.by import By

def test_search_products(driver):
    driver.get('http://127.0.0.1:5000/')

    kw = 'iPhone'
    search = driver.find_element(By.CSS_SELECTOR, '#collapsibleNavbar > form > input')
    search.send_keys(kw)
    btn = driver.find_element(By.CSS_SELECTOR, '#collapsibleNavbar > form > button')
    btn.click()
    time.sleep(1)

    results = driver.find_elements(By.CSS_SELECTOR, '.container .card-title')

    for r in results:
        assert kw in r.text

def test_login_from_cart(driver):
