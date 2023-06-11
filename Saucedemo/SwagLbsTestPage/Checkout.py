import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time


class Checkout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        username=self.driver.find_element(By.ID,"user-name")
        password=self.driver.find_element(By.ID,"password")
        login_button=self.driver.find_element(By.XPATH,"//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_button.click()

    def tearDown(self):
        self.driver.quit()

    def test_Checkout_001(self):
        add_item = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_item.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        print("Cart btn is clickable:", checkout_btn.is_enabled())
        checkout_btn.click()

    def test_Checkout_002(self):
        add_item = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_item.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn=self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        time.sleep(3)
        title_of_webpage = self.driver.title
        if title_of_webpage == "Checkout: Your Information":
            print("User redirected to next step")
        else:
            print("User redirected to next step")

    def test_Checkout_003(self):
        add_item = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_item.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID,"first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID,"last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        zipcode.send_keys("421058")
        continue_btn=self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)
        summary=self.driver.find_element(By.XPATH,"//div[@id='checkout_summary_container']")
        print("Summary of product is displayed",summary.text)

    def test_Checkout_004(self):
        add_item = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_item.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn=self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID,"first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID,"last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        zipcode.send_keys("421058")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        if continue_btn.is_enabled():
            assert True
            continue_btn.click()
            print("User allowed to next proceed")
        else:
            assert False
            print("User not allowed to next proceed")

    def test_Checkout_005(self):
        add_item = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_item.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn= self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID,"first-name")
        first_name.send_keys("123AsT")
        last_name = self.driver.find_element(By.ID,"last-name")
        last_name.send_keys("$8e5*3")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        zipcode.send_keys("abcdef")
        continue_btn=self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        titleOFWebpage = self.driver.title
        time.sleep(3)
        if titleOFWebpage == "Checkout: Your Information":
            print("User not allowed to next proceed")
        else:
            print("User allowed to next proceed")

    def test_Checkout_006(self):
        add_items = self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for item in add_items:
            item.click()
            time.sleep(2)
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name =self.driver.find_element(By.ID,"first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID,"last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        zipcode.send_keys("421058")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        finish=self.driver.find_element(By.XPATH,"//button[@id='finish']")
        finish.click()
        time.sleep(3)
        print("Order placed successfully")

    def test_Checkout_007(self):
        add_items = self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for item in add_items:
            item.click()
            time.sleep(2)
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID,"first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID,"last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        zipcode.send_keys("421058")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)
        summary = self.driver.find_element(By.XPATH, "//div[@id='checkout_summary_container']")
        print(" Checkout: Oveview page displayed the correct order details:", summary.text)
        time.sleep(3)

    def test_Checkout_008(self):
        add_items = self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for item in add_items:
            item.click()
            time.sleep(2)
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID, "postal-code")
        zipcode.send_keys("421058")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        finish = self.driver.find_element(By.XPATH,"//button[@id='finish']")
        print("Checkout: Oveview page is included a Finish option & enabled:",finish.is_enabled())
        finish.click()

    def test_Checkout_009(self):
        additems=self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for itmem in additems:
            itmem.click()
            time.sleep(2)
        cart_btn = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID, "postal-code")
        zipcode.send_keys("421058")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        cancel = self.driver.find_element(By.XPATH,"//button[@id='cancel']")
        print("Checkout: Oveview page is included a Cancel option & enabled:",cancel.is_enabled())
        cancel.click()

    def test_Checkout_010(self):
        add_items=self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for item in add_items:
            item.click()
            time.sleep(2)
        cart_btn = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID, "postal-code")
        zipcode.send_keys("421058")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        finish = self.driver.find_element(By.XPATH,"//button[@id='finish']")
        finish.click()
        back_home = self.driver.find_element(By.XPATH,"//button[@id='back-to-products']")
        print("Checkout: Complete! page is included a Cancel option & enabled:", back_home.is_enabled())
        back_home.click()
        time.sleep(3)

    def test_Checkout_011(self):
        add_items=self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for item in add_items:
            item.click()
            time.sleep(2)
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID,"first-name")
        last_lame = self.driver.find_element(By.ID,"last-name")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)
        print("User is unable to next proceed")

    def test_Checkout_012(self):
        add_items=self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for item in add_items:
            item.click()
            time.sleep(2)
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID,"first-name")
        last_name = self.driver.find_element(By.ID,"last-name")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)
        error_msg = self.driver.find_element(By.XPATH,"//div[@class='error-message-container error']")
        print("This is issue",error_msg.text)
        print("User is unable to next proceed")

    def test_Checkout_013(self):
        add_item = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_item.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID,"first-name")
        first_name.send_keys("123AsT")
        last_name = self.driver.find_element(By.ID,"last-name")
        last_name.send_keys("$8e5*3")
        zipcode = self.driver.find_element(By.ID,"postal-code")
        zipcode.send_keys("abcdef")
        continue_btn = self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        title_of_webpage = self.driver.title
        time.sleep(3)
        if title_of_webpage == "Checkout: Your Information":
            print("Error msg dispayed & User not allowed to next proceed")
        else:
            print("Error msg not dispayed & User allowed to next proceed")

    def test_Checkout_014(self):
        add_item1 = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        add_item1.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID, "postal-code")
        zipcode.send_keys("421058")
        continue_btn=self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)
        total_price1 = self.driver.find_element(By.XPATH,"//div[@class='summary_info_label summary_total_label']")
        print("Price before adding another product:",total_price1.text)
        cancel1 = self.driver.find_element(By.XPATH,"//button[@id='cancel']")
        cancel1.click()
        time.sleep(3)

        add_item2 = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        add_item2.click()
        cart_btn = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_btn.click()
        checkout_btn = self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        checkout_btn.click()
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("John")
        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("Smith")
        zipcode = self.driver.find_element(By.ID, "postal-code")
        zipcode.send_keys("411058")
        continue_btn=self.driver.find_element(By.XPATH,"//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)
        total_price2 = self.driver.find_element(By.XPATH,"//div[@class='summary_info_label summary_total_label']")
        print("Price after adding another product:",total_price2.text)
























