from unittest import TestCase

from src.data_type.int16 import Int16


class TestInt16(TestCase):

    def test_initialization(self):
        int16 = Int16(10)
        self.assertEqual(int16.value, 10)

        int16 = Int16(70000)
        self.assertEqual(int16.value, 4464)

    def test_repr(self):
        int16 = Int16(10)
        self.assertEqual(repr(int16), "Int16(10)")

    def test_addition(self):
        int16_1 = Int16(10)
        int16_2 = Int16(20)
        result = int16_1 + int16_2
        self.assertEqual(result.value, 30)

    def test_comparison(self):
        int16_1 = Int16(10)
        int16_2 = Int16(20)
        self.assertTrue(int16_1 < int16_2)
        self.assertFalse(int16_1 > int16_2)

        int16_1 = Int16(30)
        int16_2 = Int16(20)
        self.assertTrue(int16_1 > int16_2)
        self.assertFalse(int16_1 < int16_2)

    def test_bitwise_operations(self):
        int16_1 = Int16(0b1010)
        int16_2 = Int16(0b1100)
        result = int16_1 & int16_2
        self.assertEqual(result.value, 0b1000)

    def test_shift_operations(self):
        int16 = Int16(0b1010)
        result = int16 << 2
        self.assertEqual(result.value, 0b101000)

    def test_to_bits(self):
        int16 = Int16(10)
        self.assertEqual(int16.to_bits(), "0000000000001010")

    def test_to_pyint(self):
        int16 = Int16(10)
        self.assertEqual(int16.to_pyint(), 10)
