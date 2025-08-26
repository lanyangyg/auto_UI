from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.log import log


#   selenium基础操作的封装
class BasePage:
    """封装Selenium常用操作的基础页面类"""

    def __init__(self, driver, timeout=10):     #初始化方法，接收driver对象
        """
        初始化方法
        :param driver: WebDriver实例
        :param timeout: 默认等待超时时间(秒)
        """
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):        #查找单个元素，加入显式等待
        #locator 元素定位元组  (By, 表达式)
        """
        查找单个元素（带显式等待）
        :param locator: 元素定位器元组 (By, 表达式)
        :return: WebElement对象
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            log.info(f"元素定位成功：{locator}")
            return element
        except TimeoutException:
            log.error(f"元素查找超时：{locator}")
            raise

    def click_element(self, locator):       #点击元素
        element = self.find_element(locator)
        element.click()
        log.info(f"点击元素：{locator}")

    def input_text(self, locator, text):        #输入文本    #
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        log.info(f"在元素：{locator}中输入文本{text}")

    def get_text(self, locator):        #获取元素文本
        element = self.find_element(locator)
        text = element.text
        log.info(f"获取文本：{locator}->{text}")
        return text

    def is_element_visible(self, loactor):      #检查元素是否可见
        try:
            self.find_element(loactor)
            return True
        except TimeoutException:
            return False


    def find_elements(self, locator):
        return self.driver.find_elements(*locator)