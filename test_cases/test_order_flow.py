import pytest
from pages.products_page import ProductsPage
from conftest import logged_in_success_browser

@pytest.mark.run(order=2)
class TestOrder:

    def test_complete_order_flow(self, logged_in_success_browser):     # 使用已登录状态的浏览器
        # 从商品页面选择商品
        product_page = ProductsPage(logged_in_success_browser)

        # 选择商品后跳转对应详情页
        detail_page = product_page.select_product_by_name('Sauce Labs Backpack')

        # 在详情页点击加入购物车，再点击购物车按钮跳转购物车页面
        cart_page = detail_page.add_to_cart_from_details()

        # 购物车页面验证购物车中只有1件商品
        assert cart_page.get_cart_item_count() == 1

        # 购物车页面点击结帐，跳结帐页
        shipping_info_page = cart_page.start_checkout()

        # 结帐页面填写地址，跳预览页
        overview_page = shipping_info_page.enter_shipping_info('test', 'ui', '123456')

        # 预览页点完成按钮，跳完成页
        complete_page = overview_page.finish_checkout()

        # 验证是否完成订单
        assert complete_page.verify_is_checkout_complete()
