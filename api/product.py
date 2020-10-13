import logging

import requests, app


class ProductApi:
    """商品类"""

    def __init__(self):
        # 商品分类地址
        self.product_classify_url = app.base_url + '/category/all'

        # 分类下商品地址
        self.classify_product_url = app.base_url + '/product/by_category'

        # 商品信息地址
        self.detail_product_url = app.base_url + '/product/{}'

    def product_api(self):
        """商品分类接口"""
        logging.info('商品--商品分类')
        return requests.get(self.product_classify_url)

    def classify_product_api(self, classify_id=2):
        """商品下的分类"""

        logging.info('商品--分类下的商品')
        data = {"id": classify_id}
        logging.info('请求数据：{}'.format(data))
        return requests.get(self.classify_product_url, params=data)

    def detail_product_api(self, product_id=2):
        """商品信息"""
        logging.info('商品--商品信息')
        return requests.get(self.detail_product_url.format(product_id) )
