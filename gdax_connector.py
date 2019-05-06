"""Test for websockets."""
from websocket import WebSocketApp
from json import dumps, loads
from pprint import pprint

URL = "wss://ws-feed.gdax.com"

def on_message(_, message):
    pass

def on_open(socket):
    params = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}]
    }
    socket.send(dumps(params)) #send a str with socket


def main():
    ws = WebSocketApp(URL, on_open=on_open, on_message=on_message)
    ws.run_forever()

if __name__ == "__main__":
    main()