from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()

    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), "$100"))

    button = browser.find_element(By.CSS_SELECTOR, 'button#book')
    button.click()

    x_elem = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_val = int(x_elem.text)

    y = calc(x_val)

    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(y)

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button#solve')
    submit_btn.click()

    time.sleep(15)

finally:

    browser.quit()