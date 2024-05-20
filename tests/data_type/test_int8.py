from unittest import TestCase

from src.data_type.int8 import Int8


class TestInt8(TestCase):

    def test_initialization(self):
        int8 = Int8(10)
        self.assertEqual(int8.value, 10)

        int8 = Int8(300)
        self.assertEqual(int8.value, 44)

    def test_repr(self):
        int8 = Int8(10)
        self.assertEqual(repr(int8), "Int8(10)")

    def test_addition(self):
        int8_1 = Int8(10)
        int8_2 = Int8(20)
        result = int8_1 + int8_2
        self.assertEqual(result.value, 30)

    def test_comparison(self):
        int8_1 = Int8(10)
        int8_2 = Int8(20)
        self.assertTrue(int8_1 < int8_2)
        self.assertFalse(int8_1 > int8_2)

        int8_1 = Int8(30)
        int8_2 = Int8(20)
        self.assertTrue(int8_1 > int8_2)
        self.assertFalse(int8_1 < int8_2)

    def test_bitwise_operations(self):
        int8_1 = Int8(0b1010)
        int8_2 = Int8(0b1100)
        result = int8_1 & int8_2
        self.assertEqual(result.value, 0b1000)

    def test_shift_operations(self):
        int8 = Int8(0b1010)
        result = int8 << 2
        self.assertEqual(result.value, 0b101000)

    def test_to_bits(self):
        int8 = Int8(10)
        self.assertEqual(int8.to_bits(), "0000000000001010")

    def test_to_pyint(self):
        int8 = Int8(10)
        self.assertEqual(int8.to_pyint(), 10)
