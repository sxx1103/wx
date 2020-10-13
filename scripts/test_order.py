import logging

from api.apiFactory import ApiFactory
import utils


class TestOrderApi:

    def test_order_api(self):
        res = ApiFactory.get_order_api().get_order_api()
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言响应状态码
        utils.comman_assert_method(res)
        # 断言当前页面为第一页
        assert res.json().get('current_page') == 1
        # 断言订单数据大于0
        assert len(res.json()) > 0
        # 断言关键字段
        assert [i in res.text for i in ['id', 'order_no', 'total_price']]

    def test_create_order_api(self):
        res = ApiFactory.get_order_api().create_order_api(7, 3)
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言响应状态码
        utils.comman_assert_method(res)
        # 订单编号 和 订单id 不为空
        assert len(res.json().get("order_no")) > 0 and len(res.json().get("order_id")) > 0

        # 断言订单是否通过
        assert res.json().get("pass") is True

    def test_check_order_api(self):
        res = ApiFactory.get_order_api().check_order_api(121)
        logging.info('请求地址：{}'.format(res.url))
        logging.info('响应数据：{}'.format(res.json()))
        # 断言响应状态码
        utils.comman_assert_method(res)
        # 断言订单id
        assert res.json().get("id") == 121

        # 断言地址 用户名 手机号
        assert res.json().get("snap_address").get("name") == "小笼包"
        assert res.json().get("snap_address").get("mobile") == "15139715195"
