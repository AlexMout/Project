from json import loads, dumps

class Tick:
    def __init__(self,price,volume,timestamp):
        self.price = price
        self.volume = volume
        self.timestamp = timestamp
