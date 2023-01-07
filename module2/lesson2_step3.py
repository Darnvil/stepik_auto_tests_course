import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1, num2 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text), int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    answer = num1 + num2

    select = Select(browser.find_element(By.CSS_SELECTOR, "select"))
    select.select_by_visible_text(str(answer))

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    btn.click()

    time.sleep(15)

finally:
    browser.quit()