import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return math.log(abs(12 * math.sin(x)))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_val = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(int(x_val))

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    robo_checkbox = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    robo_checkbox.click()

    robo_radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robo_radiobtn.click()

    send_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    send_btn.click()

    time.sleep(20)

finally:

    browser.quit()