import pytest
from conftest import logged_in_success_browser
from pages.products_page import ProductsPage
from resources.test_data.add_remove_data import ADD_REMOVE_TEST_DATA

@pytest.mark.run(order=3)
class TestHomeToCheckout:
    #参数化加购列表和移除列表

    # @pytest.mark.parametrize(
    #     "add_list, remove_list",
    #     [
    #         (["Sauce Labs Backpack", "Sauce Labs Bike Light"], ["Sauce Labs Bike Light"]),
    #         (["Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket"], ["Sauce Labs Bolt T-Shirt"]),
    #     ]
    # )       # 内联参数化（Inline Parametrization）

    @pytest.mark.parametrize('add_list, remove_list', ADD_REMOVE_TEST_DATA)     # 外部数据参数化（External Data Parametrization）
    def test_home_to_check(self, logged_in_success_browser, add_list, remove_list):

        # 实例化浏览器，确保已登录
        product_page = ProductsPage(logged_in_success_browser)

        # 批量添加商品
        product_page.home_add_to_cart(add_list)

        # 批量移除商品
        product_page.home_remove(remove_list)

        # 点击首页购物车跳转购物车页面
        cart_page = product_page.home_shipping()

        # 购物车断言商品数量
        assert cart_page.get_cart_item_count() == len(set(add_list) - set(remove_list))     # 先把两个列表转成集合，自动去重，再用len()得到去重后的剩余数量

        # 购物车页面点击开始结帐，跳转信息填写页面
        info_page = cart_page.start_checkout()

        # 输入运输信息并跳转订单预览页面
        overview_page = info_page.enter_shipping_info('test02', 'ui', '1234')

        # 点击完成按钮跳转结帐完成页面
        complete_page = overview_page.finish_checkout()

        # 断言是否结帐完成
        assert complete_page.verify_is_checkout_complete()

        # 点击返回首页按钮返回首页
        complete_page.back_to_home()
