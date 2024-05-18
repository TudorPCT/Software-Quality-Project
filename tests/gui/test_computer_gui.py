import unittest
from unittest.mock import MagicMock
from tkinter import Tk
from threading import Thread
import time
from src.gui.computer_gui import ComputerGUI


class TestComputerGUI(unittest.TestCase):

    def setUp(self):
        self.gui = ComputerGUI()

    def test_initial_state(self):
        self.assertIsInstance(self.gui.window, Tk)
        self.assertIsNone(self.gui._ComputerGUI__computer_thread)
        self.assertIsNone(self.gui._ComputerGUI__killer_thread)

    def test_run_with_computer_thread(self):
        self.test_flag = False

        def set_flag():
            self.test_flag = True

        mock_kill_callback = MagicMock(side_effect=lambda window: window.after(100, window.quit))
        self.gui.run(set_flag, mock_kill_callback)

        self.assertFalse(self.gui._ComputerGUI__computer_thread.is_alive())
        self.assertFalse(self.gui._ComputerGUI__killer_thread.is_alive())
        self.assertTrue(self.test_flag)

    def test__computer_runner(self):
        mock_computer_thread_fn = MagicMock()
        self.gui._ComputerGUI__computer_runner(mock_computer_thread_fn)
        time.sleep(2)  # wait for bootup
        mock_computer_thread_fn.assert_called_once()

    def test__kill_runner(self):
        mock_kill_callback = MagicMock()
        self.gui._ComputerGUI__kill_runner(mock_kill_callback)
        time.sleep(2)  # wait for kill
        mock_kill_callback.assert_called_once_with(self.gui.window)


if __name__ == '__main__':
    unittest.main()
