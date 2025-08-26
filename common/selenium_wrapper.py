from selenium import webdriver
from selenium.webdriver import Chrome, Firefox
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#   封装WebDriver的一些方法
class WebDriverWrapper:
    # #   初始化浏览器 (创建一个封装了WebDriver初始化的函数)
    #
    # def init_driver(driver_type='chrome'):
    #     if driver_type == 'chrome':
    #         return webdriver.Chrome()
    #     elif driver_type == 'firefox':
    #         return webdriver.Firefox()
    #     # 可以根据需要添加更多浏览器支持
    #     else:
    #         raise ValueError("Unsupported driver type")

    # #  封装元素定位方法 (创建一些常用的元素定位方法，例如通过ID、名称、XPath等定位元素)
    # def find_element(driver, by, value):
    #     try:
    #         if by == 'id':
    #             return driver.find_element(By.ID, value)
    #         elif by == 'name':
    #             return driver.find_element(By.NAME, value)
    #         elif by == 'xpath':
    #             return  driver.find_element(By.XPATH, value)
    #         # 可以根据需要添加更多定位方式
    #         else:
    #             raise ValueError("Unsupported locator type")
    #     except NoSuchElementException:
    #         print(f"Element not found with {by}: {value}")
    #         return None
    #
    # #   封装等待方法 (封装等待直到元素可见或可点击的方法)
    # def wait_for_element(driver, by, value, timeout=10):    # 最多等待10秒，直到元素可见，否则抛出 TimeoutException
    #     try:
    #         element = WebDriverWait(driver, timeout).until(
    #             EC.visibility_of_element_located((getattr(By, by.upper()), value))
    #         )
    #         # EC.visibility_of_element_located((getattr(By, by.upper()), value)) 是 Selenium 中用于显式等待元素可见的预期条件（Expected Condition）表达式。
    #         # 用法：element = wait.until(EC.visibility_of_element_located((By.ID, "element_id")))
    #         return element
    #     except TimeoutException:
    #         print(f"Timed out waiting for element with {by}: {value}")
    #         return None


    def __init__(self, browser='chrome'):
        self.driver = Chrome() if browser.lower() == 'chrome' else Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self, locator_type, locator_value):
        by_map = {
            'id': By.ID,
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'name': By.NAME,
            'class': By.CLASS_NAME,
            'link': By.LINK_TEXT
        }
        try:
            return self.wait.until(
                EC.presence_of_element_located((by_map[locator_type], locator_value))
            )
        except TimeoutException:
            raise Exception(f"Element not found: {locator_type}={locator_value}")


    #   封装元素操作方法
    def click(self, locator_type, locator_value):
        element = self.find_element(locator_type, locator_value)
        element.click()

    def input_text(self, locator_type, locator_value, text):
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator_type, locator_value):
        return self.find_element(locator_type, locator_value).text

    def close(self):
        self.driver.quit()

