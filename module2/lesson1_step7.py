import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return math.log(abs(12 * math.sin(x)))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    x_val = treasure.get_attribute("valuex")

    y = calc(int(x_val))

    answer_input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer_input.send_keys(y)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click()

    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    btn.click()


    time.sleep(20)

finally:
    browser.quit()