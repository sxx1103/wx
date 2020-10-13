import logging

import requests, app


class OrderApi:
    """订单类"""

    def __init__(self):
        # 获取用户订单列表地址
        self.get_order_list_url = app.base_url + '/order/by_user?page=1'
        # 创建订单
        self.create_order_url = app.base_url + '/order'
        # 查看订单
        self.check_order_url = app.base_url + '/order/{}'

    def get_order_api(self, page=1):
        """
        获取订单列表
        :param page: 订单页数
        :return:
        """
        logging.info('订单--订单列表')
        data = {"page": page}
        logging.info('请求数据：{}'.format(data))
        return requests.get(self.get_order_list_url, headers=app.headers, params=data)

    def create_order_api(self, product_id, count):
        """
        创建订单
        :param product_id: 商品id
        :param count: 商品数量
        :return:
        """
        logging.info('订单--创建订单')
        data = {"products": [{"product_id": product_id, "count": count}]}
        logging.info('请求数据：{}'.format(data))
        return requests.post(self.create_order_url, json=data, headers=app.headers)

    def check_order_api(self, order_id):
        """
        查看订单
        :param order_id: 订单编号
        :return:
        """
        logging.info('订单--查看订单')
        return requests.get(self.check_order_url.format(order_id), headers=app.headers)
