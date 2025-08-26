from time import sleep

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage

class ProductsPage(BasePage):

    # 通用定位器,避免硬编码特定元素ID，使用通用定位器和文本匹配
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, ".inventory_item_img")

    # 实例化driver，并且继承basepage里面的所有方法
    def __init__(self, driver):
        super().__init__(driver)

    # 动态查找所有商品
    def select_product_by_name(self, product_name):
        #  返回一个商品列表来进行批量操作，find_elements：用于定位一组元素（例如：商品列表、搜索结果、表格行等）
        items = self.find_elements(self.PRODUCT_ITEMS)

        for item in items:
            # 在单个商品元素中查找商品名称
            name = item.find_element(*self.PRODUCT_NAMES).text      # 这里*是Python的解包操作符，用于将元组转换为独立的函数参数
            if name == product_name:
                # 点击匹配的商品
                item.find_element(*self.PRODUCT_NAMES).click()

                return ProductDetailsPage(self.driver)

        # 未找到商品时抛出异常
        raise ValueError(f"can not find product:{product_name}")


    # Swag Labs 的商品列表页面有多个商品，每个商品都是一个独立的容器（通常用 div包裹），每个容器内都有一个add/remove按钮
    # 当前页面新增add_to_cart_btn和remove_btn元素。真正定位时写成了 (By.XPATH, self.ADD_BTN)，所以不需要再包一层 By.CSS_SELECTOR
    HPD_ADD_TO_CART_BTN = ".//button[text()='Add to cart']"     # HPD-->HOME PRODUCT
    HPD_REMOVE_BTN = ".//button[text()='Remove']"
    HPD_SHIPPING_CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    # 定义一个新的查找商品div的方法，方法名前加下划线代表这个内部（私有）方法
    def _find_card_by_name(self, product_name):
        # 获取所有商品项
        items = self.find_elements(self.PRODUCT_ITEMS)      #self.find_elements(self.PRODUCT_ITEMS)获取页面上所有商品卡片元素
        # 遍历商品项
        for item in items:
            # 提取商品名称
            name = item.find_element(*self.PRODUCT_NAMES).text
            # 名称匹配
            if name == product_name:
                # 返回匹配项
                return item
        # 异常处理
        raise ValueError(f"can not find product:{product_name}")

    # 定义一个从首页点击加入购物车的方法
    def home_add_to_cart(self, product_list):
        """接收单个商品并加购"""
        # # 通过_find_hpd_by_name方法根据商品名称找到对应的商品卡片元素
        # item = self._find_card_by_name(product_name)
        # # 点击PD_ADD_TO_CART_BTN
        # item.find_element(By.XPATH, self.HPD_ADD_TO_CART_BTN).click()
        """接收 list[str]，逐个加购"""
        for product_name in product_list:
            card = self._find_card_by_name(product_name)
            card.find_element(By.XPATH, self.HPD_ADD_TO_CART_BTN).click()
        sleep(1)

    # 定义一个从首页点击移除购物车的方法
    def home_remove(self, product_list):
        """接收单个商品并移除"""
        # # 通过_find_hpd_by_name方法根据商品名称找到对应的商品卡片元素
        # item = self._find_card_by_name(product_name)
        # # 点击PD_REMOVE_BTN
        # item.find_element(By.XPATH, self.HPD_REMOVE_BTN).click()
        """接收 list[str]，逐个移除"""
        for product_name in product_list:
            card = self._find_card_by_name(product_name)
            card.find_element(By.XPATH, self.HPD_REMOVE_BTN).click()
        sleep(1)

    # 定义一个从首页跳转购物车页面的方法
    def home_shipping(self):
        self.find_element(self.HPD_SHIPPING_CART).click()
        # 跳转到CartPage
        return CartPage(self.driver)
