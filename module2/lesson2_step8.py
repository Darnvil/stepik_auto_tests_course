import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "firstname").send_keys("111")
    browser.find_element(By.NAME, "lastname").send_keys("222")
    browser.find_element(By.NAME, "email").send_keys("333")

    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
    file_load = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    file_load.send_keys(filepath)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(15)

finally:
    browser.quit()