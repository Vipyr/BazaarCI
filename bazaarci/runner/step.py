from threading import Event, Thread
from typing import Callable, Optional

from bazaarci.runner.node import Node
from bazaarci.runner import Product


class Step(Node):
    def __init__(self, name, graph: Optional["Graph"] = None, target: Optional[Callable] = None):
        super().__init__(name, graph)
        self._consumes = set()
        self._produces = set()
        self.target = target
        self.thread = None
        self.output = None
        if self.graph is not None:
            self.graph.add(self)

    def produces(self, item: str = None):
        if item is None:
            return self._produces
        if isinstance(item, str):
            item = Product.from_name(item)
        self._produces.add(item)

    def consumes(self, item: str = None):
        if item is None:
            return self._consumes
        if isinstance(item, str):
            item = Product.from_name(item)
        self._consumes.add(item)

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        [product.wait() for product in self.consumes()]
        if self.target is not None:
            self.output = self.target()
        [product.set() for product in self.produces()]

    def wait(self):
        if self.thread and self.thread.is_alive():
            self.thread.join()

    def __str__(self):
        return self.name

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.name)
