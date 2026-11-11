import pytest
from base import logger
from pages.enter_home_page import EnterHomePage
from pages.login_page import LoginPage
from utils.tools import read_json


class TestLogin:
    """测试登录"""
    args_names = "username, password,expect_result,img"

    @pytest.mark.parametrize(args_names, read_json("login_data.json"))
    def test_00_login(self, first_app_driver, username, password, expect_result, img):
        """测试登录成功"""
        try:
            # 前置：进入首页
            EnterHomePage(first_app_driver).enter_home()
            # 1.创建对象
            login_page = LoginPage(first_app_driver)
            # 2.调用方法
            login_page.enter_login()
            login_page.email_login(username, password)
            # 判断
            if img == "login_success":
                result = login_page.base_get_text(login_page.success_result_loc)
            else:
                result = login_page.base_get_toast(login_page.fail_result_loc)
            # 记录日志
            logger.info(f"登录结果: {result}")
            # 3.断言
            assert expect_result in result
            # 4.截图
            login_page.base_get_shot(img)
        except Exception as e:
            logger.error(e)
            raise
