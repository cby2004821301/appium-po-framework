# 项目配置文件
import os

# 项目根目录
BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)
# appium接口地址
APPIUM_SERVER = "http://127.0.0.1:4723"
# 设备配置信息
DEVICE_CONFIG = {
    "automationName": "UiAutomator2",  # 自动化引擎（appium）
    "platformName": "Android",  # 移动端系统平台（Android或iOS）
    "platformVersion": "12",  # 平台对应版本（必须和设备OS版本一致）
    "deviceName": "mumu",  # 设备名称，可以自定义
    # "waitForIdleTimeout": 1000,  # 减少等待界面“空闲”的时间
    # "waitForSelectorTimeout": 0,  # 查找元素超时设为0（配合代码里的显式等待）
}
# app本身配置
APP_CONFIG = {
    "appPackage": "com.netease.yanxuan",  # 包名
    "appActivity": ".SplashActivityDefault",  # Activity页面名
    "noReset": True,  # 不清除数据,保留登录状态
}
# 第一次启动app
FIRST_APP_CONFIG = {
    "appPackage": "com.netease.yanxuan",  # 包名
    "appActivity": ".SplashActivityDefault"  # Activity页面名
}