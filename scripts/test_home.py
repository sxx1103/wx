"""首页测试脚本"""
import logging

from api.apiFactory import ApiFactory
import utils


class TestHome(object):

    def test_banner_api(self):
        res = ApiFactory.get_home_api().banner_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言响应状态码
        utils.comman_assert_method(res)
        # 断言id和name
        assert res.json().get("id") == 1 and res.json().get("name") == "首页置顶"
        # 断言items长度大于0
        assert len(res.json().get("items")) > 0

    def test_theme_api(self):
        res = ApiFactory.get_home_api().theme_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言响应状态码
        utils.comman_assert_method(res)

        # 断言关键字段是否存在
        assert False not in [i in res.text for i in ['"id":1', '"id":2', '"id":3']]
        # 断言关键字段是否存在
        assert False not in [i in res.text for i in ['name', 'topic_img', 'head_img']]

    def test_recent_product_api(self):
        res = ApiFactory.get_home_api().recent_product_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))

        # 断言响应状态码
        utils.comman_assert_method(res)

        # 断言关键字是否存在
        assert 'id' in res.text and 'name' in res.text and 'price' in res.text
