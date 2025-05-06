import logging
import time

from megabit.lib.request_utils import send_request


def get_all_quotation_tickers(url, method: str, headers=None, payload=None):
    """
    获取K线数据
    :param url: 请求的URL
    :param method: 请求的方法，GET
    :param headers: 请求的头部信息
    :param payload: 请求的参数
    :return: 请求的响应结果

    """
    # 记录当前的时间戳（单位：毫秒）到日志中，方便后续调试和监控
    logging.info("当前时间:%s", str(int(time.time() * 1000)))
    # 调用 megabit.lib.request_utils 模块中的 send_request 函数发送请求，并返回请求结果
    return send_request(method, url, headers, payload)


if __name__ == '__main__':
    # 5.4 获取所有交易对行情
    base_api_url = "https://open.hashex.vip"
    api_url = base_api_url + "/spot/v1/p/quotation/tickers"
    resp_json = get_all_quotation_tickers(api_url, "GET", None, None)
    assert resp_json["code"] == 0
    assert resp_json["msg"] == "success"
    assert resp_json["data"] is not None
