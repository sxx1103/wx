"""设置配置信息"""
import logging.handlers, os


def log_conf():
    """定义日志方法"""
    log_path = './log'
    # 设置日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 设置处理器--控制台处理器
    sh = logging.StreamHandler()
    # 设置处理器--控制台处理器
    trfh = logging.handlers.TimedRotatingFileHandler(filename=log_path + os.sep + "mini.log",
                                                     when='midnight', interval=1, backupCount=7, encoding='utf-8')

    # 设置格式化器
    f = "%(asctime)s -- %(levelname)s --" \
        " (%(filename)s --%(funcName)s  -- %(lineno)d ) --%(message)s "
    fmt = logging.Formatter(f)

    # 处理器添加格式化器
    sh.setFormatter(fmt)
    trfh.setFormatter(fmt)

    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(trfh)

# 接口通用配置
base_url = 'http://e.cn/api/v1'

# 微信code
code='071ptdGa1gJcNz0evVIa1pLnIV2ptdGr'

# 通用请求头
headers = {"Content-Type": "application/json", "token": "f703dfd65e5082cf87f518aa3e6d3e0e"}
