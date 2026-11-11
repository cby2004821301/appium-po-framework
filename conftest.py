# 导包
import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config import *
from pages.enter_home_page import EnterHomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage


@pytest.fixture(scope="function")
def first_app_driver():
    """初始：无缓存的前后置"""
    # 配置移动端设备信息
    des_caps = {**DEVICE_CONFIG, **FIRST_APP_CONFIG}
    # 初始化设备配置信息
    option = UiAutomator2Options().load_capabilities(des_caps)
    # 创建驱动对象
    driver = webdriver.Remote(APPIUM_SERVER, options=option)
    # 返回值
    yield driver
    # 暂停3秒
    try:
        driver.terminate_app(FIRST_APP_CONFIG['appPackage'])
    except Exception:
        pass
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def app_driver():
    """有缓存的前后置"""
    # 配置移动端设备信息
    des_caps = {**DEVICE_CONFIG, **APP_CONFIG}
    # 初始化设备配置信息
    option = UiAutomator2Options().load_capabilities(des_caps)
    # 创建驱动对象
    driver = webdriver.Remote(APPIUM_SERVER, options=option)
    # 返回值
    yield driver
    # 暂停3秒
    time.sleep(3)
    # 关闭app
    driver.terminate_app(APP_CONFIG['appPackage'])
    # 关闭驱动
    driver.quit()


@pytest.fixture(scope="function")
def login_ok(first_app_driver):
    """登录成功前置"""
    # 进入首页
    EnterHomePage(first_app_driver).enter_home()
    # 1.创建对象
    login_page = LoginPage(first_app_driver)
    # 2.调用方法
    login_page.enter_login()
    login_page.email_login("test_user@example.com", "your_password")
    # 3.退出APP
    time.sleep(3) # 确保APP登录进入了
    first_app_driver.terminate_app(FIRST_APP_CONFIG['appPackage'])


@pytest.fixture
def search_ok(app_driver):
    """搜索成功前置"""
    SearchPage(app_driver).search("毛巾")
    return app_driver
