from base import logger
from pages.search_page import SearchPage


class TestSearch:
    """测试搜索"""

    def test_search_success(self, app_driver):
        """测试搜索"""
        try:
            # 前置：进入搜索页面
            # 1.创建对象
            search_page = SearchPage(app_driver)
            # 2.调用方法
            search_page.search("毛巾")
            # 3.获取结果
            result = search_page.base_get_text(search_page.result_loc)
            logger.info(f"搜索结果: {result}")
            # 4.断言
            assert "毛巾" in result
            # 5.截图
            search_page.base_get_shot("search_success")
        except Exception as e:
            logger.error(f"搜索异常: {str(e)}")
            raise
