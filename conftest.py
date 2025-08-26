# from time import sleep
# import pytest
# from selenium import webdriver
# from setting import ENV
# from common.log import log
#
# # 将公共 fixture 放在 conftest.py 中，无需导入即可全局使用
# # pytest.fixture 是 Pytest 测试框架的核心功能，主要用于管理测试的前置条件和后置清理工作，实现测试环境的模块化和复用。
# # 通过 scope 定义生命周期（class：每个测试类执行一次）
# @pytest.fixture(scope="class")
# def login():        #pytest fixture是独立函数，不需要也不应该包含self参数。self仅在类方法中使用。
#     # 前置操作（打开浏览器，跳转页面，最大化等等）
#     log.info("初始化浏览器")
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     log.info(f"打开URL: {ENV.url}")
#     driver.get(ENV.url)
#     driver.implicitly_wait(10)         # 隐式等待加载元素，全局，10秒内
#
#     # 通过 yield 或 return 分隔前置操作（如数据库连接）和后置清理（如关闭连接），避免重复代码
#     yield driver      # 必须要返回测试用的对象/数据，testcase中才能使用。必须通过 yield 返回一个值来支持迭代操作（如 for 循环或 next() 调用
#     sleep(2)
#     driver.quit()     # 后置清理
#     log.info("关闭浏览器")



import pytest
from selenium import webdriver
from common.log import log
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser():      #初始化/使用/销毁浏览器
    """初始化浏览器驱动"""
    log.info("启动浏览器")

    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # 测试结束后关闭浏览器
    log.info("关闭浏览器")
    driver.quit()

@pytest.fixture(scope="session")
def logged_in_success_browser(browser):
    browser.delete_all_cookies()
    # 添加：先导航到登录页面
    browser.get('https://www.saucedemo.com/')

    # 已登录状态浏览器会话
    login_page = LoginPage(browser)
    login_page.login(username='standard_user', password='secret_sauce')

    assert "inventory.html" in browser.current_url
    yield browser  # 已登录的 driver

    # # 确保导航到homepage（添加显式等待）
    # if "inventory.html" not in browser.current_url:
    #     browser.get('https://www.saucedemo.com/inventory.html')
    #
    # assert "Swag Labs" in browser.title
    # yield browser
