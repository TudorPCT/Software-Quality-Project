from src.data_type.int8 import Int8
from src.data_type.int16 import Int16
from unittest.mock import MagicMock, Mock
import unittest
import os
from src.memory.main_memory import MainMemory
from pathlib import Path


RES_DIR = os.path.join(str(Path(__file__).parent.absolute()), "resources")


class TestMainMemory(unittest.TestCase):

    def test_memory_size_arg(self):
        self.assertRaises(AssertionError, lambda: MainMemory(500, []))
        MainMemory(1024, [])
        MainMemory(2048, [])
        self.assertRaises(AssertionError, lambda: MainMemory(3000, []))
        self.assertRaises(AssertionError, lambda: MainMemory(131072, []))

    def test_automatic_assignments(self):
        peripheral1 = Mock()
        peripheral1.get_necessarily_memory_size = Mock(return_value=Int8(100))
        peripheral1.configure_memory = Mock()
        peripheral1.print_report = Mock()

        peripheral2 = Mock()
        peripheral2.get_necessarily_memory_size = Mock(return_value=Int8(10))
        peripheral2.configure_memory = Mock()
        peripheral2.print_report = Mock()

        main_memory = MainMemory(1024, [peripheral1, peripheral2])
        peripheral1.configure_memory.assert_called_with(main_memory, Int16(923))
        peripheral2.configure_memory.assert_called_with(main_memory, Int16(913))

        self.assertTrue(main_memory.get_stack_base() == Int16(911))

    def test_config_assignments_and_memory_calls(self):
        peripheral1 = Mock()
        peripheral1.get_necessarily_memory_size = Mock(return_value=Int8(100))

        peripheral2 = Mock()
        peripheral2.get_necessarily_memory_size = Mock(return_value=Int8(10))

        main_memory = MainMemory(1024, [peripheral1, peripheral2], [Int16(924), Int16(914)], Int16(900))
        peripheral1.configure_memory.assert_called_with(main_memory, Int16(924))
        peripheral2.configure_memory.assert_called_with(main_memory, Int16(914))

        self.assertTrue(main_memory.get_stack_base() == Int16(900))

    def test_get_set_item_in_memory(self):
        main_memory = MainMemory(1024, [])
        main_memory[Int16(100)] = Int16(24)
        main_memory[Int16(102)] = Int16(2)
        main_memory[Int16(104)] = Int16(2001)

        self.assertTrue(main_memory[Int16(100)] == Int16(24))
        self.assertTrue(main_memory[Int16(102)] == Int16(2))
        self.assertTrue(main_memory[Int16(104)] == Int16(2001))

        self.assertTrue(main_memory[Int16(105)] == Int16((2001 & 255) << 8))

    def test_get_set_in_peripheral(self):
        peripheral1 = Mock()
        peripheral1.get_necessarily_memory_size = Mock(return_value=Int8(128))
        peripheral1.in_range = lambda idx: Int16(886) <= idx <= (Int16(886) + Int16(128))
        peripheral1.assigned_memory_idx = Int16(886)
        peripheral1.__getitem__ = Mock(return_value=Int8(4))
        peripheral1.__setitem__ = Mock()

        peripheral2 = Mock()
        peripheral2.get_necessarily_memory_size = Mock(return_value=Int8(1))
        peripheral2.in_range = lambda idx: Int16(880) <= idx <= (Int16(880) + Int16(1))
        peripheral2.assigned_memory_idx = Int16(880)
        peripheral2.__getitem__ = Mock(return_value=Int8(10))
        peripheral2.__setitem__ = Mock()

        main_memory = MainMemory(1024, [peripheral1, peripheral2], [Int16(886), Int16(880)], Int16(870))

        self.assertTrue(main_memory[Int16(890)] == Int16(4))
        self.assertTrue(main_memory[Int16(880)] == Int16(10))

        main_memory[Int16(900)] = Int16(63)
        main_memory[Int16(880)] = Int16(58)
        peripheral1.__setitem__.assert_called_with(Int16(14), Int8(63))
        peripheral2.__setitem__.assert_called_with(Int16(0), Int8(58))


