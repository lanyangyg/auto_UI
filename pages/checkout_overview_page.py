from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.checkout_complete_page import CheckoutCompletePage

#   Checkout step 2
class CheckoutOverviewPage(BasePage):

    FINISH_BTN = (By.ID, "finish")

    # 实例化driver，并且继承basepage里面的所有方法
    def __init__(self, driver):
        super().__init__(driver)

    def finish_checkout(self):
        self.click_element(self.FINISH_BTN)
        return CheckoutCompletePage(self.driver)