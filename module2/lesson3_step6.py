import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    time.sleep(1)

    browser.switch_to.window(browser.window_handles[1])

    x_val = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    y = calc(x_val)

    input_answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(15)

finally:
    browser.quit()