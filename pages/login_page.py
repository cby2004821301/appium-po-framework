from appium.webdriver.common.appiumby import By
from base.base_page import BasePage


class LoginPage(BasePage):
    """登录页面"""

    def __init__(self, driver):
        super().__init__(driver)
        # 元素定位器
        # 个人按钮
        self.mine_loc = (By.XPATH, '//android.widget.TextView[@text="个人"]')
        # 更多按钮
        self.more_loc = (By.XPATH, '(//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/img_icon"])[2]')
        # 其他按钮
        self.other_loc = (By.ID, 'com.netease.yanxuan:id/newOtherLoginTypes')
        # 勾选协议
        self.agree_loc = (By.ID, 'com.netease.yanxuan:id/check_box')
        # 邮箱按钮
        self.email_loc = (By.XPATH, '(//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/img_icon"])[4]')
        # 账号
        self.username_loc = (By.CLASS_NAME, 'android.widget.AutoCompleteTextView')
        # 密码
        self.password_loc = (By.ID, 'com.netease.yanxuan:id/password_edit')
        # 登录按钮
        self.login_loc = (By.ID, 'com.netease.yanxuan:id/btn_login_content')
        # 成功结果元素定位
        self.success_result_loc = (By.ID, 'com.netease.yanxuan:id/user_name')
        # 失败结果元素定位 //android.widget.Toast[@text="账号或密码错误"]
        self.fail_result_loc = (By.XPATH, '//android.widget.Toast')

    def enter_login(self):
        """进入登录页面"""
        self.base_click(self.mine_loc)
        self.base_click(self.more_loc)
        self.base_click(self.other_loc)
        self.base_click(self.agree_loc)
        self.base_click(self.email_loc)

    def email_login(self, username, password):
        """邮箱登录"""
        self.base_input_text(self.username_loc, "test_user@example.com")
        self.base_input_text(self.password_loc, "your_password")
        self.base_click(self.login_loc)
