import unittest
from src.data_type.int16 import Int16
from unittest.mock import MagicMock
from src.peripheral.peripherial import Peripheral


class TestPeripheral(unittest.TestCase):

    def setUp(self):
        self.peripheral = Peripheral()
        self.memory_mock = MagicMock()  # Mocking MainMemory
        self.assigned_memory_idx = Int16(10)

    def test_initial_state(self):
        self.assertIsNone(self.peripheral.memory)
        self.assertIsNone(self.peripheral.assigned_memory_idx)

    def test_configure_memory(self):
        self.peripheral.configure_memory(self.memory_mock, self.assigned_memory_idx)
        self.assertEqual(self.peripheral.memory, self.memory_mock)
        self.assertEqual(self.peripheral.assigned_memory_idx, self.assigned_memory_idx)


if __name__ == '__main__':
    unittest.main()
