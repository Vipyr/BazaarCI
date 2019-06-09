from functools import reduce
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
        # The ability to call item.set() is necessary for outputs.
        elif hasattr(item, "set") and callable(item.set):
            self._produces.add(item)

    def consumes(self, item: str = None):
        if item is None:
            return self._consumes
        # The ability to call item.wait() is necessary for inputs.
        elif hasattr(item, "wait") and callable(item.wait):
            self._consumes.add(item)

    def start(self):
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        [product.wait() for product in self.consumes()]
        # Once all inputs are available, check that there are unset outputs.
        # If all output products have already been set, then this step is
        # not required to run.
        if reduce(lambda x, y: x and y.wait(0), self.produces(), True):
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
