from base import logger
from pages.enter_home_page import EnterHomePage
from pages.login_page import LoginPage


class TestLogin:
    """测试登录"""

    def test_01_login_success(self, first_app_driver):
        """测试登录成功"""
        # 前置：进入首页
        EnterHomePage(first_app_driver).enter_home()
        # 1.创建对象
        login_page = LoginPage(first_app_driver)
        # 2.调用方法
        login_page.enter_login()
        login_page.email_login("test_user@example.com", "your_password")
        # 记录日志
        result = login_page.base_get_text(login_page.success_result_loc)
        logger.info(f"登录结果: {result}")
        # 3.断言
        assert '用户' in result
        # 4.截图
        login_page.base_get_shot("login_success")

    def test_02_login_fail_pwd_error(self, first_app_driver):
        """测试登录成功"""
        # 前置：进入首页
        EnterHomePage(first_app_driver).enter_home()
        # 1.创建对象
        login_page = LoginPage(first_app_driver)
        # 2.调用方法
        login_page.enter_login()
        login_page.email_login("test_user@example.com", "Aa1234")
        # 记录日志
        result = login_page.base_get_toast(login_page.fail_result_loc)
        logger.info(f"登录结果: {result}")
        # 3.断言
        assert '账号或密码错误' in result
        # 4.截图
        login_page.base_get_shot("login_pwd_error")

    def test_03_login_fail_username_error(self, first_app_driver):
        """测试登录成功"""
        # 前置：进入首页
        EnterHomePage(first_app_driver).enter_home()
        # 1.创建对象
        login_page = LoginPage(first_app_driver)
        # 2.调用方法
        login_page.enter_login()
        login_page.email_login("invalid_email", "Aa1234567")
        # 记录日志
        result = login_page.base_get_toast(login_page.fail_result_loc)
        logger.info(f"登录结果: {result}")
        # 3.断言
        assert '账号格式错误' in result
        # 4.截图
        login_page.base_get_shot("login_username_error")
