from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from common.log import log

#   登录页面操作封装
class LoginPage(BasePage):
    # 页面元素定位器（Element Locators，专门用于在网页上定位特定的 UI 元素
    USERNAME = (By.ID, "user-name")  # 推荐改用ID选择器
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    APP_LOGO = (By.CLASS_NAME, "app_logo")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        # 添加显式等待确保元素加载
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        )

        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
        log.info(f"尝试登录: 用户名={username}")
        sleep(2)

    def get_error_message(self):    #获取错误提示文本
        return self.get_text(self.ERROR_MESSAGE)

    def get_logo_text(self):    #获取登录后页面Logo文本
        return self.get_text(self.APP_LOGO)

