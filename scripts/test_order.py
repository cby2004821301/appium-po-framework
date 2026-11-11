from pages.order_page import OrderPage


class TestOrder:
    """订单测试"""

    def test_order(self, app_driver):
        """订单测试"""
        # 创建订单页面对象
        order_page = OrderPage(app_driver)
        # 调用下单方法
        order_page.order()
        # 断言
        # 截图
        order_page.base_get_shot("order_ok")
