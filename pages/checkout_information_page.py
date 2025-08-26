from time import sleep
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.checkout_overview_page import CheckoutOverviewPage

#   Checkout step 1
class CheckoutInformationPage(BasePage):
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="last-name"]')
    ZIP_CODE_INPUT = (By.XPATH, '//input[@id="postal-code"]')
    CONTINUE_BTN = (By.XPATH, '//input[@id="continue"]')


    # 实例化driver，并且继承basepage里面的所有方法
    def __init__(self, driver):
        super().__init__(driver)

    def enter_shipping_info(self, firstname, lastname, zipcode):    # 传firstname, lastname, zipcode到输入框中
        self.input_text(self.FIRST_NAME_INPUT, firstname)
        self.input_text(self.LAST_NAME_INPUT, lastname)
        self.input_text(self.ZIP_CODE_INPUT, zipcode)
        sleep(1)
        self.click_element(self.CONTINUE_BTN)   # 点击continue，跳转到CheckoutOverviewPage
        return CheckoutOverviewPage(self.driver)

