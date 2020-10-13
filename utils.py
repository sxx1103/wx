def comman_assert_method(res, code=200):
    """
    断言响应状态码
    :param res: 响应对象
    :param code:状态码
    :return:
    """

    assert res.status_code == code
