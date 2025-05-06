import logging
import time
import uuid

from megabit.lib.authentication import gen_Signature
from megabit.lib.request_utils import send_request


def get_balance_spot(url, method, accessKey, secretKey, params):
    current_milliseconds = str(int(time.time() * 1000))
    logging.info("当前时间:%s", current_milliseconds)

    signature = gen_Signature(secretKey, params, current_milliseconds)
    # 生成随机字符串作为 X-Request-Nonce，防止重放攻击，并取一半长度
    full_nonce = str(uuid.uuid4())
    nonce = full_nonce[:len(full_nonce) // 2]
    Headers = {"X-Access-Key": accessKey, "X-Signature": signature, "X-Request-Timestamp": current_milliseconds,
               "X-Request-Nonce": nonce}
    logging.info("Headers:%s", Headers)
    logging.info("create new order request params:%s", params)
    responses = send_request(method, url, Headers, params)
    return responses


if __name__ == '__main__':
    base_api_url = "https://open.hashex.vip"
    accessKey = "252b48701a3710ed91e01c18438f45b52f0c0e1f87f94d744bb7ec0aa5e0cb50"
    secretKey = "0c9700838a36e36d4ad691dba044203b5ce7913c911e3ea83a9664abd042e491"

    api_url = base_api_url + "/spot/v1/u/balance/spot"
    params = {

    }
    get_balance_spot(api_url, "GET", accessKey, secretKey, params)
