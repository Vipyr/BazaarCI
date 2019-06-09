from unittest import TestCase
from unittest.mock import MagicMock, patch
from bazaarci.runner.step import set_run_behavior, wait_for_producers, skip_if_redundant


class TestStepRunBehavior(TestCase):
    def test_set_run_behavior(self):
        mock_Step = MagicMock()
        mock_Decorator1 = MagicMock()
        mock_Decorator2 = MagicMock()
        set_run_behavior(mock_Step, mock_Decorator1, mock_Decorator2)
        mock_Decorator2.assert_called_once_with(mock_Step._run)
        mock_Decorator1.assert_called_once_with(mock_Decorator2.return_value)

    def test_wait_for_producers(self):
        mock_Step = MagicMock()
        mock_run = MagicMock()
        mock_Step.consumes.return_value = [MagicMock()]
        wrapped_run = wait_for_producers(mock_run)
        wrapped_run(mock_Step)
        mock_Step.consumes.assert_called_once_with()
        mock_Step.consumes.return_value[0].wait.assert_called_once_with()
        mock_run.assert_called_once_with(mock_Step)

    def test_skip_if_redundant(self):
        with self.subTest("No output Products"):
            mock_Step = MagicMock()
            mock_run = MagicMock()
            mock_Step.produces.return_value = []
            wrapped_run = skip_if_redundant(mock_run)
            wrapped_run(mock_Step)
            mock_run.assert_called_once_with(mock_Step)
        with self.subTest("Unset output Product"):
            # The output Product is not set, run
            mock_Step = MagicMock()
            mock_run = MagicMock()
            mock_Step.produces.return_value = [MagicMock()]
            mock_Step.produces.return_value[0].wait.return_value = False
            wrapped_run = skip_if_redundant(mock_run)
            wrapped_run(mock_Step)
            mock_run.assert_called_once_with(mock_Step)
        with self.subTest("Set output Product"):
            # The output Product is set, skip run
            mock_Step = MagicMock()
            mock_run = MagicMock()
            mock_Step.produces.return_value = [MagicMock()]
            mock_Step.produces.return_value[0].wait.return_value = True
            wrapped_run = skip_if_redundant(mock_run)
            wrapped_run(mock_Step)
            mock_run.assert_not_called()
