import json
import logging
import time
from logging import handlers
from config import *
from appium import webdriver
from appium.options.android import UiAutomator2Options


# class DriverTools:
#     """app驱动的封装"""
#
#     # 类属性：初始的APP驱动
#     driver = None
#
#     @classmethod
#     def get_app_driver(cls):
#         """创建APP驱动"""
#         if cls.driver is None:
#             # 配置移动端设备信息
#             des_caps = {**DEVICE_CONFIG, **APP_CONFIG}
#             # 初始化设备配置信息
#             option = UiAutomator2Options().load_capabilities(des_caps)
#             # 创建驱动对象
#             cls.driver = webdriver.Remote(APPIUM_SERVER, options=option)
#         return cls.driver
#
#     @classmethod
#     def quit_app_driver(cls):
#         """退出APP驱动"""
#         if cls.driver:
#             time.sleep(3)
#             cls.driver.quit()
#             cls.driver = None


def read_json(file_name):
    """
    读取JSON文件并转换为格式为 [(), (), ...] 的列表
    :param file_name: json文件名
    :return: 列表
    """
    data = []  # 空列表
    file_path = BASE_DIR + "/data/" + file_name  # JSON文件路径
    # 打开JSON文件
    with open(file_path, mode='r', encoding='utf-8') as f:
        # 读取JSON文件并解析为Python对象【列表套字典】
        tmp = json.load(f)
        for i in tmp:
            a = tuple(i.values())
            data.append(a)
        # 返回列表
        return data


class GetLog:
    # 日志器
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = BASE_DIR + "/log/" + "app-{}.log".format(time.strftime("%Y%m%d"))
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,  # 日志文件名
                                                           when="midnight",  # 日志归档时间
                                                           interval=1,  # 每天归档一次
                                                           backupCount=3,  # 保留3天日志
                                                           encoding="utf-8")  # 日志编码格式
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log
