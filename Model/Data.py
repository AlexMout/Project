from json import loads, dumps

class Data:
    def __init__(self):
        self._data = []
        self.run = True

    @property
    def data(self):
        return self.data

    def add_data(self,tick):
        self._data.append(tick)

    def __str__(self):
        return dumps(self.__dict__)
