from bazaar.step import Step
from bazaar.web.rendersvg import svg


class Graph(Step, set):
    def __init__(self, graph=None):
        super().__init__(graph, "GRAPH", target=self.run)

    def start(self):
        [step.start() for step in self]

    def run(self):
        pass
