from selenium.webdriver.common.by import By

from base.base_page import BasePage


class SearchPage(BasePage):
    """搜索页面"""

    def __init__(self, driver):
        super().__init__(driver)
        # 元素定位器
        # 搜索框
        self.search_loc = (By.CLASS_NAME, "android.widget.TextSwitcher")
        # 内容框
        self.content_loc = (By.ID, "com.netease.yanxuan:id/search_input")
        # 搜索按钮
        self.search_btn_loc = (By.ID, "com.netease.yanxuan:id/tv_search_button")
        # 搜索成功结果
        self.result_loc = (By.XPATH,
                           '(//android.widget.TextView[@resource-id="com.netease.yanxuan:id/tv_goods_name"])[1]')

    def search(self, content):
        """搜索"""
        self.base_click(self.search_loc)
        self.base_input_text(self.content_loc, content)
        self.base_click(self.search_btn_loc)
