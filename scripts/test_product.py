import logging

from api.apiFactory import ApiFactory
import utils

class TestProduct:

    def test_product_api(self):
        res = ApiFactory.get_product_api().product_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))

        # 断言状态码
        utils.comman_assert_method(res)
        # 断言关键字
        assert False not in [i in res.text for i in ['id', 'name', 'img']]
        # 断言字段长度
        assert len(res.json()) > 0

    def test_classify_product_api(self):
        res = ApiFactory.get_product_api().classify_product_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))

        # 断言状态码
        utils.comman_assert_method(res)

        # 断言关键字
        assert [i in res.text for i in ['id', 'name', 'price', 'stock', 'main_img_url']]

        # 断言字段长度
        assert len(res.json()) > 0

    def test_detail_product_api(self):
        res = ApiFactory.get_product_api().detail_product_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))

        # 断言状态码
        utils.comman_assert_method(res)

        # 断言关键字
        assert res.json().get('id') == 2 and res.json().get('name') == '梨花带雨 3个'

        # 断言价格
        assert res.json().get('price') == '0.01'
