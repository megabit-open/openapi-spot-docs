import logging
import time
import uuid


from megabit.lib.authentication import gen_Signature
from megabit.lib.request_utils import send_request

def batch_cancel_order(url,method:str, api_Access, api_secret, create_new_order_params, current_milliseconds):
    logging.info("当前时间:%s", current_milliseconds)

    signature = gen_Signature(api_secret, create_new_order_params, current_milliseconds)
    full_nonce = str(uuid.uuid4())
    nonce = full_nonce[:len(full_nonce) // 2]
    Headers = {"X-Access-Key": api_Access, "X-Signature": signature, "X-Request-Timestamp": current_milliseconds,
               "X-Request-Nonce": nonce}
    logging.info("Headers:%s", Headers)
    logging.info("create new order request params:%s", create_new_order_params)
    resp_json = send_request(method, url, Headers, create_new_order_params)
    return resp_json

if __name__ == '__main__':
    # 指定订单号批量取消
    base_api_url = "https://open.hashex.vip"
    accessKey = "252b48701a3710ed91e01c18438f45b52f0c0e1f87f94d744bb7ec0aa5e0cb50"
    secretKey = "0c9700838a36e36d4ad691dba044203b5ce7913c911e3ea83a9664abd042e491"

    api_url = base_api_url + "/spot/v1/u/trade/order/batch/cancel"

    current_milliseconds = str(int(time.time() * 1000))

    batch_cancel_order_params = {
        "orderIdsJson": '["483375804806646784","483375804810841088"]'
    }
    batch_cancel_order(api_url, "POST",accessKey, secretKey, batch_cancel_order_params, current_milliseconds)
