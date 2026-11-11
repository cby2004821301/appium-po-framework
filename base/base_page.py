import os
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base import logger
from config import BASE_DIR


class BasePage:
    def __init__(self, driver):
        """初始化APP驱动"""
        self.driver = driver

    def fd_element(self, locator, timeout=10):
        """
        定位单个元素（带显式等待）
        :param locator: 元组类型的定位器
        :param timeout: 超时时间
        :return: 元素
        """
        try:
            logger.info(f"定位元素: {locator}")
            element = (WebDriverWait(self.driver, timeout)
                       .until(EC.visibility_of_element_located(locator)))  # 元素可见
            return element
        except Exception as e:
            logger.error(f"元素定位失败: {locator} - {str(e)}")
            raise

    def fd_elements(self, locator, timeout=15):
        """定位多个元素（带显式等待）"""
        try:
            logger.info(f"定位多个元素: {locator}")
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
        except Exception as e:
            logger.error(f"元素组定位失败: {locator} - {str(e)}")
            raise

    def base_click(self, locator):
        """点击元素"""
        logger.info(f"点击元素: {locator}")
        self.fd_element(locator).click()

    def base_input_text(self, locator, text):
        """
        输入文本
        :param locator: 输入框的元素定位器
        :param text: 输入内容
        :return: 无
        """
        logger.info(f"在元素 {locator} 输入文本: {text}")
        element = self.fd_element(locator)
        element.clear()  # 清空文本框
        element.send_keys(text)  # 输入文本

    def base_get_text(self, locator):
        """获取元素文本"""
        text = self.fd_element(locator).text
        logger.info(f"获取元素文本: {locator} -> {text}")
        return text

    def base_swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        """滑动操作"""
        logger.info(f"滑动操作: ({start_x},{start_y}) -> ({end_x},{end_y})")
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def base_get_toast(self, toast_loc, timeout=5):
        """获取Toast提示文本"""
        try:
            # toast_loc = (By.XPATH, '//android.widget.Toast')
            toast = WebDriverWait(self.driver, timeout, poll_frequency=0.1).until(
                EC.presence_of_element_located(toast_loc))  # 元素存在
            text = toast.text
            logger.info(f"获取Toast提示: {text}")
            return text
        except Exception as e:
            logger.error(f"获取Toast失败: {str(e)}")
            return ""

    def base_get_shot(self, file_name):
        """
        截图
        :param file_name: 截图文件名
        :return:无
        """
        # 推荐
        now = datetime.now().strftime("%Y%m%d%H%M%S")  # 按照指定格式生成当前时间
        # 保存指定的位置
        file_path = os.path.join(BASE_DIR, 'img', f"{file_name}_{now}.png")
        self.driver.get_screenshot_as_file(file_path)

    def is_element_exist(self, locator, timeout=2):
        """
        检查元素是否存在（不抛异常）
        :param locator: 元素定位器
        :param timeout: 超时时间（默认2秒）
        :return: True/False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
