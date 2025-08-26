# import pytest
# from time import sleep
# from pages.login_page import LoginPage
# from setting import ENV
# from conftest import login
#
# class TestLogin:
#     @pytest.mark.parametrize('username, password, expected_result', [
#         ("standard_user", "pwd123456", "Epic sadface: Username and password do not match any user in this service"),
#         ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
#         ("standard_user", "secret_sauce", "Swag Labs")
#     ], ids=["test_login_01", "test_login_02", "test_login_03"])
#
#     def test_login(self, username, password, expected_result, login):
#         """
#         登录功能测试
#         :param username: 用户名
#         :param password: 密码
#         :param expected_result: 预期结果
#         :param login: conftest提供的fixture，返回浏览器驱动
#         """
#         driver = login
#         login_page = LoginPage(driver)
#
#         # 打开被测网址
#         driver.get(ENV.url)
#
#         # 执行登录操作
#         login_page.login(username, password)
#         sleep(1)  # 等待页面加载
#
#         # 根据预期结果类型进行断言
#         if expected_result.startswith("Epic sadface"):
#             # 错误提示断言
#             actual_error = login_page.get_error_message()
#             assert actual_error == expected_result
#         else:
#             # 登录成功后页面元素断言
#             logo_text = login_page.get_logo_text()
#             assert logo_text == expected_result


import pytest
from pages.login_page import LoginPage
from resources.test_data.login_data import LOGIN_TEST_DATA
from conftest import browser

@pytest.mark.run(order=1)
class TestLogin:
    @pytest.mark.parametrize('username, password, expected', LOGIN_TEST_DATA)
    def test_login(self, browser, username, password, expected):    # 使用browser而不是logged_in_success_browser
        """
        登录功能测试
        :param username: 用户名
        :param password: 密码
        :param expected: 预期结果
        :param browser: 浏览器驱动实例
        """

        # 打开登录页面
        browser.get("https://www.saucedemo.com/")

        login_page = LoginPage(browser)

        # 执行登录
        login_page.login(username, password)

        # 验证结果
        if expected.get("error"):
            assert login_page.get_error_message() == expected["error"]
        else:
            assert login_page.get_logo_text() == expected["success"]
