import unittest
from unittest.mock import MagicMock, patch
from src.peripheral.peripherial import Int16, Int8
from src.gui.computer_gui import ComputerGUI
import tkinter as tk
from src.peripheral.screen_peripheral import ScreenPeripheral


class TestScreenPeripheral(unittest.TestCase):

    def setUp(self):
        self.screen = ScreenPeripheral()
        self.memory_mock = MagicMock()  # Mocking MainMemory
        self.assigned_memory_idx = Int16(10)
        self.screen.configure_memory(self.memory_mock, self.assigned_memory_idx)

    def test_initial_state(self):
        self.assertEqual(len(self.screen.pixels), ScreenPeripheral.lines_nr.to_pyint())
        self.assertEqual(len(self.screen.pixels[0]), ScreenPeripheral.cols_nr.to_pyint())
        self.assertIsNone(self.screen.main_frame)

    def test_get_necessarily_memory_size(self):
        expected_memory_size = Int8(16) * Int8(12)
        self.assertEqual(self.screen.get_necessarily_memory_size(), expected_memory_size)

    def test_in_range(self):
        idx_within_range = Int16(10)
        idx_outside_range = Int16(500)
        self.assertTrue(self.screen.in_range(idx_within_range))
        self.assertFalse(self.screen.in_range(idx_outside_range))

    @patch('builtins.print')
    def test_print_report(self, mock_print):
        self.screen.print_report()
        expected_output = (
            f"Peripheral name: ScreenPeripheral\n"
            f"Assigned memory address: {self.assigned_memory_idx}\n"
            f"Memory size: {self.screen.get_necessarily_memory_size()}\n"
            f"{'=' * 20}\n"
        )
        mock_print.assert_called_once_with(expected_output)

    def test_configure_gui(self):
        root = MagicMock(spec=ComputerGUI)
        root.window = tk.Tk()  # We need an actual Tk instance to avoid TclError
        self.screen.configure_gui(root)
        self.assertIsNotNone(self.screen.main_frame)
        self.assertEqual(len(self.screen.main_frame.winfo_children()), ScreenPeripheral.lines_nr.to_pyint() * ScreenPeripheral.cols_nr.to_pyint())

    def test_setitem(self):
        self.screen.pixels = [[tk.Label() for _ in range(ScreenPeripheral.cols_nr.to_pyint())]
                              for _ in range(ScreenPeripheral.lines_nr.to_pyint())]
        idx = Int8(5)
        val = Int8(65)  # ASCII code for 'A'
        self.screen.__setitem__(idx, val)
        line_idx = idx.to_pyint() // ScreenPeripheral.cols_nr.to_pyint()
        col_idx = idx.to_pyint() % ScreenPeripheral.cols_nr.to_pyint()
        self.assertEqual(self.screen.pixels[line_idx][col_idx].cget('text'), chr(val.to_pyint()))


if __name__ == '__main__':
    unittest.main()
