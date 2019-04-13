from threading import Thread

from bazaar.product import Product
from bazaar.web.rendersvg import svg


class Step:
    def __init__(self, graph, name, target=None):
        self.graph = graph
        self.name = name
        self.consumes = set()
        self.produces = set()
        self.target = target
        if self.graph is not None:
            self.graph.add(self)

    def start(self):
        thread = Thread(target=self.run)
        thread.start()

    def run(self):
        [product.wait() for product in self.consumes]
        self.target()
        [product.set() for product in self.produces]

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Step({})".format(self.name)
