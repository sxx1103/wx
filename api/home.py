import logging

import requests, app


class HomeApi(object):
    """轮播图类"""

    def __init__(self):
        # 轮播图地址
        self.banner_url = app.base_url + '/banner/{}'
        #     专题栏地址
        self.theme_url = app.base_url + '/theme'
        #     最近新品地址
        self.recent_product_url = app.base_url + '/product/recent'

    def banner_api(self, num=1):
        """
        请求轮播图
        :param num: 轮播图页面数
        :return:
        """
        logging.info('首页--轮播图')
        return requests.get(self.banner_url.format(num))

    def theme_api(self, ids='1,2,3'):
        """
        专题栏方法
        params:专题栏页数
        :return:
        """
        logging.info('首页--专题栏')
        # 请求数据
        data = {"ids": ids}
        logging.info('请求数据：{}'.format(data))
        return requests.get(self.theme_url, params=data)

    def recent_product_api(self):
        """请求最近新品"""
        logging.info('首页--最近新品')
        return requests.get(self.recent_product_url)
