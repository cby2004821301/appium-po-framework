from pages.enter_home_page import EnterHomePage


class TestHomePage:
    """测试首页"""

    def test_enter_home(self, first_app_driver):
        """测试进入首页"""
        # 前置：需要APP驱动
        # 1.创建对象
        home = EnterHomePage(first_app_driver)
        # 2.调用方法
        home.enter_home()
        # 后置：退出APP驱动
