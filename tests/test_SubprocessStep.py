from unittest import TestCase
from unittest.mock import MagicMock, patch
import subprocess

from bazaarci.runner import SubprocessStep


class TestSubprocessStep(TestCase):
    @patch("bazaarci.runner.subprocessstep.partial")
    @patch("bazaarci.runner.subprocessstep.Step")
    def test___init__(self, mock_Product, mock_partial):
        s = SubprocessStep("test", None, "test", "arg", kwarg="kwarg")
        mock_partial.assert_called_once_with(
            subprocess.run,
            "test",
            "arg",
            kwarg="kwarg",
        )
