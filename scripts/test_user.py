import logging

from api.apiFactory import ApiFactory
import app, utils, pytest


@pytest.mark.run(order=0)
class TestUserApi:

    def test_user_api(self):
        """获取token"""
        res = ApiFactory.get_user_api().get_token_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))

        # 断言状态码
        utils.comman_assert_method(res)
        # 断言关键字
        assert len(res.json()) > 0
        app.headers['token'] = res.json().get('token')
        print(app.headers)

    def test_verify_token(self):
        res = ApiFactory.get_user_api().verify_token_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言状态码
        utils.comman_assert_method(res)

        # 断言关键字长度
        assert res.json().get('isValid') is True

    def test_get_information(self):
        res = ApiFactory.get_user_api().get_information_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言状态码
        utils.comman_assert_method(res)
        #  断言关键字段
        assert False not in [i in res.text for i in ['小笼包', "15139715195", "上海市", "浦东新区", "111号"]]

        # 断言字段长度
        assert len(res.json()) > 0
