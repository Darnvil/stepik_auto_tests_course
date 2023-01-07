import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    x_val = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = calc(x_val)

    input_ans = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input_ans.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(15)

finally:
    browser.quit()