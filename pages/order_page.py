from base.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy,By


class OrderPage(BasePage):
    """订单页面"""

    def __init__(self,driver):
        super().__init__(driver)
        # 点击购物图标
        self.cart_icon_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="购物车"]')
        # 点击结算按钮
        # 1.直接定位 # 固定一个商品
        # self.settlement_btn_loc = (AppiumBy.XPATH, '//android.widget.TextView[@text="结算(1)"]')
        # 2.定位结算按钮框
        # self.settlement_btn_loc = (AppiumBy.XPATH,'//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]')
        # 3.使用结算文本包含定位
        self.settlement_btn_loc = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"结算")]')
        # 点击提交订单按钮
        self.order_btn_loc = (AppiumBy.ID, 'com.netease.yanxuan:id/order_btn')

    def order(self):
        """提交订单"""
        self.base_click(self.cart_icon_loc)
        self.base_click(self.settlement_btn_loc)
        self.base_click(self.order_btn_loc)