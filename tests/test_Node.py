from unittest import TestCase
from bazaarci.runner.node import Node


class TestNode(TestCase):
    def test_produces(self):
        n = Node("test")
        with self.assertRaises(NotImplementedError):
            n.produces()

    def test_consumes(self):
        n = Node("test")
        with self.assertRaises(NotImplementedError):
            n.consumes()

    def test_start(self):
        n = Node("test")
        with self.assertRaises(NotImplementedError):
            n.start()

    def test_run(self):
        n = Node("test")
        with self.assertRaises(NotImplementedError):
            n.run()
