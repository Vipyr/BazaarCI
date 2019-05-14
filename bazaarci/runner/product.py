from threading import Event


class Product(Event):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return "Product({})".format(self.name)
