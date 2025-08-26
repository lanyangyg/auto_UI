from time import sleep
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.cart_page import CartPage


class ProductDetailsPage(BasePage):
    PRODUCT_TITLE = (By.CLASS_NAME, 'inventory_details_name large_size')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart')
    SHOPPING_CART_BTN = (By.CSS_SELECTOR, '.shopping_cart_link')

    # 实例化driver，并且继承basepage里面的所有方法
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    def add_to_cart_from_details(self):
        self.click_element(self.ADD_TO_CART_BTN)        # 点击ADD_TO_CART，跳转到CartPage
        sleep(1)
        self.click_element(self.SHOPPING_CART_BTN)      # 点击SHOPPING_CART_BUTTON，跳转到CartPage
        return CartPage(self.driver)


