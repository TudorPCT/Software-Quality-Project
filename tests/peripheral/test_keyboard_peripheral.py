import unittest
from unittest.mock import MagicMock, patch

from src.peripheral.keyboard_peripheral import KeyboardPeripheral, keys
from src.peripheral.peripherial import Int16, Int8
from src.gui.computer_gui import ComputerGUI
import tkinter as tk


class TestKeyboardPeripheral(unittest.TestCase):

    def setUp(self):
        self.keyboard = KeyboardPeripheral()
        self.memory_mock = MagicMock()  # Mocking MainMemory
        self.assigned_memory_idx = Int16(10)
        self.keyboard.configure_memory(self.memory_mock, self.assigned_memory_idx)

    def test_initial_state(self):
        self.assertEqual(self.keyboard.keys, [])
        self.assertIsNone(self.keyboard.main_frame)

    def test_get_necessarily_memory_size(self):
        self.assertEqual(self.keyboard.get_necessarily_memory_size(), Int8(1))

    def test_in_range(self):
        self.assertTrue(self.keyboard.in_range(Int16(10)))
        self.assertFalse(self.keyboard.in_range(Int16(11)))

    @patch('builtins.print')
    def test_print_report(self, mock_print):
        self.keyboard.print_report()
        expected_output = (
            f"Peripheral name: KeyboardPeripheral\n"
            f"Assigned memory address: {self.assigned_memory_idx}\n"
            f"Memory size: {self.keyboard.get_necessarily_memory_size()}\n"
            f"{'=' * 20}\n"
        )
        mock_print.assert_called_once_with(expected_output)

    def test_push_key(self):
        key_code = Int8(65)  # ASCII code for 'A'
        self.keyboard._KeyboardPeripheral__push_key(key_code)
        self.assertEqual(self.keyboard.keys, [key_code])

    def test_configure_gui(self):
        root = MagicMock(spec=ComputerGUI)
        root.window = tk.Tk()  # We need an actual Tk instance to avoid TclError
        self.keyboard.configure_gui(root)
        self.assertIsNotNone(self.keyboard.main_frame)
        self.assertEqual(len(self.keyboard.main_frame.winfo_children()), len(keys) * len(keys[0]))

    def test_getitem(self):
        self.keyboard._KeyboardPeripheral__push_key(Int8(65))
        self.assertEqual(self.keyboard[Int8(0)], Int8(65))
        self.assertEqual(self.keyboard[Int8(0)], Int8(0))


if __name__ == '__main__':
    unittest.main()
