from unittest import TestCase, skip
from unittest.mock import MagicMock, patch
from bazaarci.runner import Step


class TestNode(TestCase):
    @patch("bazaarci.runner.step.Product")
    def test_produces(self, mock_Product):
        s = Step("test")
        with self.subTest("With Argument"):
            s.produces("rawr")
            mock_Product.from_name.assert_called_once_with("rawr")
        with self.subTest("Without Argument"):
            produces = s.produces()
            self.assertEqual(len(produces), 1)

    @patch("bazaarci.runner.step.Product")
    def test_consumes(self, mock_Product):
        s = Step("test")
        with self.subTest("With Argument"):
            s.consumes("rawr")
            mock_Product.from_name.assert_called_once_with("rawr")
        with self.subTest("Without Argument"):
            consumes = s.consumes()
            self.assertEqual(len(consumes), 1)

    @patch("bazaarci.runner.step.Thread")
    def test_start(self, mock_Thread):
        s = Step("test")
        s.start()
        self.assertIsNotNone(s.thread)
        mock_Thread.assert_called_once_with(target=s.run)

    def test_run(self):
        mock_target = MagicMock()
        s = Step("test", target=mock_target)
        s.run()
        mock_target.assert_called_once_with()
