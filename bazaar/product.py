from functools import lru_cache
from threading import Event


class Product(Event):
    @classmethod
    @lru_cache()
    def from_name(cls, name):
        return Product(name)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return "Product({})".format(self.name)
