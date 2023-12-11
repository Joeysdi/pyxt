# -*- coding:utf-8 -*-
import time
from pyxt.websocket import logger
from pyxt.websocket.spot import SpotWebsocketStreamClient

logger.initLogger()

if __name__ == '__main__':
    symbol = "btc_usdt"


    def message_handler(_, message):
        logger.info(message)


    my_client = SpotWebsocketStreamClient(on_message=message_handler,
                                          proxies={"http": "http://127.0.0.1:1088"})

    # Subscribe to a single symbol stream
    my_client.kline(symbol=symbol, interval="1m", action=SpotWebsocketStreamClient.ACTION_SUBSCRIBE)
    time.sleep(5)
    # # Unsubscribe
    my_client.kline(
        symbol=symbol, interval="1m", action=SpotWebsocketStreamClient.ACTION_UNSUBSCRIBE
    )
    time.sleep(5)
    logger.info("closing ws connection")
    my_client.stop()
