from unittest import TestCase

from bazaarci.runner import Graph, Product, Step


class TestIntegration(TestCase):
    def test_graph(self):
        g = Graph("TestGraph")
        s1 = Step("Step1", g)
        s2 = Step("Step2", g)
        s1.produces("Product1")
        s2.consumes("Product1")
        g.start()
        g.wait()
