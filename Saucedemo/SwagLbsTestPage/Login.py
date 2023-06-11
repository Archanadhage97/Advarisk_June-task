import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

    def test_LF_001(self):
        username=self.driver.find_element(By.ID,"user-name")
        password=self.driver.find_element(By.ID,"password")
        login_button=self.driver.find_element(By.XPATH,"//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        print("Login Successfully")

    def test__LF_002(self):
        username = self.driver.find_element(By.ID, "user-name").send_keys("invalid@123")
        password = self.driver.find_element(By.ID, "password").send_keys("invalidpass")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        error_msg = self.driver.find_element(By.TAG_NAME,"h3")
        print(error_msg.text)
        print("Login Unsuccessful")

    def test_LF_003(self):
        username = self.driver.find_element(By.ID, "user-name").send_keys("invalid@123")
        password = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        error_msg = self.driver.find_element(By.TAG_NAME, "h3")
        print(error_msg.text)
        print("Login Unsuccessful")

    def test_LF_004(self):
        username = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        password = self.driver.find_element(By.ID, "password").send_keys("invalidpass")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        error_msg = self.driver.find_element(By.TAG_NAME, "h3")
        print(error_msg.text)
        print("Login Unsuccessful")

    def test_LF_005(self):
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        error_msg = self.driver.find_element(By.TAG_NAME, "h3")
        print(error_msg.text)
        print("Login Unsuccessful")

    def test_LF_006(self):
        username = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        error_msg = self.driver.find_element(By.TAG_NAME, "h3")
        print(error_msg.text)
        print("Login Unsuccessful")

    def test_LF_007(self):
        username = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        password = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        error_msg = self.driver.find_element(By.TAG_NAME, "h3")
        print(error_msg.text)
        print("Login Unsuccessful")

    def test_LF_008(self):
        username=self.driver.find_element(By.ID,"user-name")
        password=self.driver.find_element(By.ID,"password")
        login_button=self.driver.find_element(By.XPATH,"//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        print("Login Successfully")
        menu_btn=self.driver.find_element(By.ID,"react-burger-menu-btn").click()
        time.sleep(5)
        logout_btn=self.driver.find_element(By.LINK_TEXT,"Logout").click()
        print("Logout Successfully")

    def test_LF_008(self):
        username=self.driver.find_element(By.ID,"user-name")
        password=self.driver.find_element(By.ID,"password")
        login_button=self.driver.find_element(By.XPATH,"//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()
        menu_btn=self.driver.find_element(By.ID,"react-burger-menu-btn").click()
        time.sleep(5)
        logout_btn=self.driver.find_element(By.LINK_TEXT,"Logout").click()
        print("Login Successfully")

    def test_LF_009(self):
        username=self.driver.find_element(By.ID,"user-name")
        password=self.driver.find_element(By.ID,"password")
        login_button=self.driver.find_element(By.XPATH,"//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        print("Login btn is worked or not:", login_button.is_enabled())
        login_button.click()
        time.sleep(5)






if __name__ == "__main__":
    unittest.main()







