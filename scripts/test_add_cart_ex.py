from base import logger
from pages.cart_page import CartPage


class TestCart:
    """购物车测试"""

    def test_add_cart(self,search_ok):
        """加入购物车测试"""
        # 前置:搜索
        # 创建购物车页面对象
        cart_page = CartPage(search_ok)
        # 调用添加购物车方法
        cart_page.enter_goods_detail()
        cart_page.add_cart()
        # 获取加入购物车结果
        result = cart_page.base_get_toast(cart_page.result_loc)
        logger.info(f"添加购物车结果: {result}")
        # 断言
        assert "加入购物车成功" in result
        # 截图
        cart_page.base_get_shot("add_cart")
        # 返回首页
        cart_page.back_home()
