import logging
import time
import uuid

from megabit.lib.authentication import gen_Signature
from megabit.lib.request_utils import send_request


def get_order_history(url, method:str,api_Access, api_secret, get_order_details_params, current_milliseconds):
    logging.info("当前时间:%s", current_milliseconds)

    signature = gen_Signature(api_secret, get_order_details_params, current_milliseconds)
    # 生成随机字符串作为 X-Request-Nonce，防止重放攻击，并取一半长度
    full_nonce = str(uuid.uuid4())
    nonce = full_nonce[:len(full_nonce) // 2]
    Headers = {"X-Access-Key": api_Access, "X-Signature": signature, "X-Request-Timestamp": current_milliseconds,
               "X-Request-Nonce": nonce}

    resp_json = send_request(method, url, Headers, get_order_details_params)
    return resp_json


if __name__ == '__main__':
    base_api_url = "https://open.hashex.vip"
    accessKey = "252b48701a3710ed91e01c18438f45b52f0c0e1f87f94d744bb7ec0aa5e0cb50"
    secretKey = "0c9700838a36e36d4ad691dba044203b5ce7913c911e3ea83a9664abd042e491"

    current_milliseconds = str(int(time.time() * 1000))

    api_url = base_api_url + "/spot/v1/u/trade/order/history"

    get_order_history_params = {
        "symbol": "BTC_USDT",
        # "startTime": 1744373221106, #2025-04-11 20:07:01
        # "endTime": 1745237221000, #2025-04-15 10:00:52
        # "balanceType": "1",
        # "id": 482370252425324032,
        # "direction": "PREV",
        "limit": "10",

    }
    get_order_history(api_url, "GET",accessKey, secretKey, get_order_history_params, current_milliseconds)
