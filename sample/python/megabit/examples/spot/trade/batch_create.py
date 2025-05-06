import logging
import time
import uuid

from megabit.lib.authentication import gen_Signature
from megabit.lib.request_utils import send_request

def batch_create_order(createOrderUrl, method:str,api_access, api_secret, create_new_order_params, current_milliseconds):
    logging.info("当前时间:%s", current_milliseconds)
    signature = gen_Signature(api_secret, create_new_order_params, current_milliseconds)
    full_nonce = str(uuid.uuid4())
    nonce = full_nonce[:len(full_nonce) // 2]
    Headers = {"X-Access-Key": api_access, "X-Signature": signature, "X-Request-Timestamp": current_milliseconds,
               "X-Request-Nonce": nonce}
    # 创建订单
    logging.info("Headers:%s", Headers)
    logging.info("create new order request params:%s", create_new_order_params)
    resp_json= send_request(method, createOrderUrl, Headers, create_new_order_params)
    return resp_json


if __name__ == '__main__':
    # 指定币对批量创建订单
    base_api_url = "https://open.hashex.vip"
    accessKey = "252b48701a3710ed91e01c18438f45b52f0c0e1f87f94d744bb7ec0aa5e0cb50"
    secretKey = "0c9700838a36e36d4ad691dba044203b5ce7913c911e3ea83a9664abd042e491"

    api_url = base_api_url + "/spot/v1/u/trade/order/batch/create"

    current_milliseconds = str(int(time.time() * 1000))

    create_new_order_params = {
        "ordersJsonStr":
            '['
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            # '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"80000","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"LIMIT","totalAmount":"0.001","price":"1","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            '{"symbol":"BTC_USDT","direction":"BUY","tradeType":"MARKET","totalAmount":"0.001","clientOrderId":"BATCH_LIMIT_BUY_123456789","balanceType":1},'
            '{"symbol":"BTC_USDT","direction":"SELL","tradeType":"LIMIT","totalAmount":"0.0001","price":"80000","clientOrderId":"BATCH_LIMIT_SELL_123456789"},'
            '{"symbol":"ETH_USDT","direction":"SELL","tradeType":"LIMIT","totalAmount":"1","price":"1","clientOrderId":"BATCH_LIMIT_SELL_123456789"},'
            '{"symbol":"BTC_USDT","direction":"SELL","tradeType":"MARKET","totalAmount":"0.001","clientOrderId":"BATCH_LIMIT_SELL_123456789"}'
            ']'
    }
    batch_create_order(api_url, "POST",accessKey, secretKey, create_new_order_params, current_milliseconds)
