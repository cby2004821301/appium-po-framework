from appium.webdriver.common.appiumby import By, AppiumBy
from base.base_page import BasePage


class CartPage(BasePage):
    """购物车页面"""

    def __init__(self, driver):
        super().__init__(driver)
        # 第一个商品图
        self.goods_img = (
            AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/img_goods"])[1]')
        # 位置权限
        self.location_btn = (AppiumBy.ID, 'com.netease.yanxuan:id/btn_alert_positive')
        # 点击加入购物车按钮
        self.cart_btn1 = (AppiumBy.XPATH, '//android.widget.TextView[@text="加入购物车"]')
        self.cart_btn2 = (AppiumBy.ID, 'com.netease.yanxuan:id/button')
        # 购物车toast提示结果
        self.result_loc = (AppiumBy.XPATH, '//android.widget.Toast')
        # 返回首页：3次操作
        self.back_loc1 = (AppiumBy.ID, 'com.netease.yanxuan:id/nav_left_text')
        self.back_loc2 = (AppiumBy.ID, 'com.netease.yanxuan:id/search_bar_return')
        # self.back_loc3 = (AppiumBy.ID, 'com.netease.yanxuan:id/search_bar_return')

    def enter_goods_detail(self):
        """进入商品详情页"""
        self.base_click(self.goods_img)
        # 判断是否弹出位置权限
        # if self.location_btn:  # 该条件永远为真True
        if self.is_element_exist(self.location_btn):
            self.base_click(self.location_btn)

    def add_cart(self):
        """加入购物车"""
        self.base_click(self.cart_btn1)
        self.base_click(self.cart_btn2)

    def back_home(self):
        """返回首页"""
        self.base_click(self.back_loc1)
        self.base_click(self.back_loc2)
        self.base_click(self.back_loc2)
