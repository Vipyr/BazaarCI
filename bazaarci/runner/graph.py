from typing import Optional

from bazaarci.runner.node import Node


class Graph(Node, set):
    def __init__(self, name: str, graph: Optional["Graph"] = None):
        super().__init__(name, graph)

    def start(self):
        [step.start() for step in self]

    def produces(self):
        for node in self:
            for product in node.produces():
                yield product

    def consumes(self):
        for node in self:
            for product in node.consumes():
                yield product

