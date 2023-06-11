import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
chromedriver_autoinstaller.install()



driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("invalid@123")
driver.find_element(By.ID, "password").send_keys("invalidpass")
time.sleep(10)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
Error_msg=driver.find_element(By.TAG_NAME,"h3")
print(Error_msg.text)
print("Login Unsuccessful")