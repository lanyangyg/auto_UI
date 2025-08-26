from selenium.webdriver.common.by import By
from base.base_page import BasePage

#   Checkout step 3
class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CSS_SELECTOR, '.complete-header')
    BACK_HOME_BTN = (By.XPATH, '//button[@id="back-to-products"]')

    # 实例化driver，并且继承basepage里面的所有方法
    def __init__(self, driver):
        super().__init__(driver)

    def verify_is_checkout_complete(self):      #用于断言是否已经完成checkout
        return 'Thank you for your order!' in self.get_text(self.COMPLETE_HEADER)

    # 加一个返回首页按钮
    def back_to_home(self):
        self.click_element(self.BACK_HOME_BTN)
