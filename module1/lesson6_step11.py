from selenium import webdriver
from selenium.webdriver.common.by import By

import time

try:

    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
    first_name_input.send_keys("Dmitry")

    last_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
    last_name_input.send_keys("kolbasko")

    email_input = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
    email_input.send_keys("1234")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    time.sleep(1)

    text = browser.find_element(By.TAG_NAME, "h1").text


    assert text == "Congratulations! You have successfully registered!"

except Exception as e:
    print(e)

finally:
    time.sleep(30)
    browser.quit()

