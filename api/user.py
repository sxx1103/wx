import logging

import app, requests


class UserApi:

    def __init__(self):
        # 获取token地址
        self.get_token_url = app.base_url + '/token/user'
        # token验证地址
        self.token_verify_url = app.base_url + '/token/verify'
        # 获取地址信息url
        self.get_information_url = app.base_url + '/address'

    def get_token_api(self):
        """token--获取token"""
        logging.info('token--获取token')
        data = {"code": app.code}
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def verify_token_api(self):
        """验证token"""
        logging.info('token--验证token')
        data = {"token": app.headers.get('token')}
        logging.info('请求数据：{}'.format(data))
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def get_information_api(self):
        """获取用户信息"""
        logging.info('token--获取用户信息')

        return requests.get(self.get_information_url,headers=app.headers)


