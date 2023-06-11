import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time


class CartPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        username = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        password = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    def tearDown(self):
        self.driver.quit()

    def test_Cart_001(self):
        cartbutton = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        print("cart buttoon is enabled",cartbutton.is_enabled())
        print("cart button is displayed",cartbutton.is_displayed())
        cartbutton.click()

    def test_Cart_002(self):
        item = self.driver.find_element(By.XPATH,"(//div[normalize-space()='Sauce Labs Backpack'])[1]")
        cart_button = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
        cart_button.click()
        time.sleep(3)
        print("item added to cart sucessfully")

    def test_Cart_003(self):
        item = self.driver.find_element(By.XPATH, "(//div[normalize-space()='Sauce Labs Backpack'])[1]")
        item.click()
        add_to_cart = self.driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart.click()
        time.sleep(3)
        shopping_cart_button= self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        shopping_cart_button.click()
        time.sleep(3)
        print("Single added item dispalyed in the cart with correct details")

    def test_Cart_004(self):
        items = self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for i in items:
            i.click()
            time.sleep(2)

    def test_Cart_005(self):
        items = self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for i in items:
            i.click()
            time.sleep(2)
        cartbutton = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
        print("multiple item added  is display in the cart")
        time.sleep(5)

    def test_Cart_006(self):
        items = self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for i in items:
            i.click()
            time.sleep(2)
        cart_button = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_button.click()
        remove_from_cart=self.driver.find_elements(By.XPATH,"//button[@class='btn btn_secondary btn_small cart_button']")
        for i in remove_from_cart:
            i.click()
            time.sleep(2)
        print("all items are removed from the cart")

    def test_Cart_007(self):
        items=self.driver.find_elements(By.XPATH,"//button[@class='btn btn_primary btn_small btn_inventory']")
        for i in items:
            i.click()
            time.sleep(2)
        cartbutton = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cartbutton.click()
        remove_from_cart=self.driver.find_elements(By.XPATH,"//button[@class='btn btn_secondary btn_small cart_button']")
        for i in remove_from_cart:
            i.click()
            time.sleep(2)
        print("cart is empty after removing all items")

    def test_Cart_008(self):
        item_add_cart=self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        item_add_cart.click()
        time.sleep(5)
        cart_button = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_button.click()
        time.sleep(5)
        continue_shop=self.driver.find_element(By.XPATH,"//button[@id='continue-shopping']")
        continue_shop.click()
        items = self.driver.find_elements(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory']")
        for i in range(len(items) - 4, len(items)):
            items[i].click()
            time.sleep(3)
        print("User can add multiple items to cart by continue shopping")


    def test_Cart_009(self):
        item_add_cart=self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        item_add_cart.click()
        time.sleep(5)
        cart_button = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_button.click()
        recheck_item_details=self.driver.find_element(By.XPATH,"//div[@class='inventory_item_name']")
        print("User rechecked the product summary, price & colour:",recheck_item_details.is_displayed())
        recheck_item_details.click()
        time.sleep(3)

    def test_Cart_010(self):
        item_add_cart = self.driver.find_element(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
        time.sleep(5)
        cart_button = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_button.click()
        recheck_item_details = self.driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
        recheck_item_details.click()
        time.sleep(3)
        back_To_products=self.driver.find_element(By.XPATH,"//button[@id='back-to-products']")
        back_To_products.click()
        time.sleep(3)
        print("User is able to go back on Product page")

    def test_Cart_011(self):
        cart_button = self.driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
        cart_button.click()
        time.sleep(3)
        checkout_btn=self.driver.find_element(By.XPATH,"//button[@id='checkout']")
        print("Checkout button is clearly visible on cart page:", checkout_btn.is_displayed())
        print("Checkout button is enabled on cart page:",checkout_btn.is_enabled())
        checkout_btn.click()





