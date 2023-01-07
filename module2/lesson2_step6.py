from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

link = "https://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_val = int(x_elem.text)

    y = calc(x_val)

    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()

    button.click()

    time.sleep(15)

finally:
    browser.quit()