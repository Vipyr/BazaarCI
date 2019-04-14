from unittest import TestCase, skip
from unittest.mock import MagicMock
from bazaarci.runner import Graph


class TestNode(TestCase):
    def test_produces(self):
        mock_Step = MagicMock()
        g = Graph("test")
        g.add(mock_Step)
        for _ in g.produces():
            pass
        mock_Step.produces.assert_called_once_with()

    def test_consumes(self):
        mock_Step = MagicMock()
        g = Graph("test")
        g.add(mock_Step)
        for _ in g.consumes():
            pass
        mock_Step.consumes.assert_called_once_with()

    def test_start(self):
        mock_Step = MagicMock()
        g = Graph("test")
        g.add(mock_Step)
        g.start()
        mock_Step.start.assert_called_once_with()

    def test_run(self):
        g = Graph("test")
        with self.assertRaises(NotImplementedError):
            g.run()
