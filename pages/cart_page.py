from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.checkout_information_page import CheckoutInformationPage


class CartPage(BasePage):

    CART_ITEM = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")

    # 实例化driver，并且继承basepage里面的所有方法
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_item_count(self):      # 用于验证购物车中商品数量
        return len(self.find_elements(self.CART_ITEM))

    def start_checkout(self):     # 点击checkout，跳转到CheckoutInformationPage
        self.click_element(self.CHECKOUT_BTN)
        return CheckoutInformationPage(self.driver)
