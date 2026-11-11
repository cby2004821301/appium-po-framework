from base.base_page import BasePage
from appium.webdriver.common.appiumby import By


class EnterHomePage(BasePage):
    """进入首页"""

    def __init__(self, driver):
        """设置属性"""
        super().__init__(driver)
        # 元素定位器
        self.agree_loc = (By.ID, "com.netease.yanxuan:id/btn_alert_positive")
        self.skip_loc = (By.XPATH, '//android.widget.TextView[@text="跳过"]')

    def enter_home(self):
        """进入首页"""
        self.base_click(self.agree_loc)
        self.base_click(self.skip_loc)
