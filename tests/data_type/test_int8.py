import unittest
from unittest import TestCase

from src.data_type.int8 import Int8


class TestInt8(TestCase):

    def test_initialization(self):
        int1 = Int8()
        self.assertEqual(int1.value, 0)

        int2 = Int8(10)
        self.assertEqual(int2.value, 10)

        int3 = Int8(-5)
        self.assertEqual(int3.value, 0)

        int4 = Int8(300)
        self.assertEqual(int4.value, 44)  # 300 % 256 = 44

    def test_repr(self):
        int16 = Int8(10)
        self.assertEqual(repr(int16), "Int8(10)")

    def test_addition(self):
        int1 = Int8(10)
        int2 = Int8(20)
        result = int1 + int2
        self.assertEqual(result.value, 30)

    def test_subtraction(self):
        int1 = Int8(20)
        int2 = Int8(10)
        result = int1 - int2
        self.assertEqual(result.value, 10)

    def test_multiplication(self):
        int1 = Int8(5)
        int2 = Int8(4)
        result = int1 * int2
        self.assertEqual(result.value, 20)

    def test_division(self):
        int1 = Int8(20)
        int2 = Int8(3)
        result = int1 / int2
        self.assertEqual(result.value, 6)

    def test_modulo(self):
        int1 = Int8(20)
        int2 = Int8(3)
        result = int1 % int2
        self.assertEqual(result.value, 2)

    def test_bitwise_and(self):
        int1 = Int8(10)
        int2 = Int8(6)
        result = int1 & int2
        self.assertEqual(result.value, 2)

    def test_bitwise_or(self):
        int1 = Int8(10)
        int2 = Int8(6)
        result = int1 | int2
        self.assertEqual(result.value, 14)

    def test_bitwise_xor(self):
        int1 = Int8(10)
        int2 = Int8(6)
        result = int1 ^ int2
        self.assertEqual(result.value, 12)

    def test_left_shift(self):
        int1 = Int8(2)
        result = int1 << 2
        self.assertEqual(result.value, 8)

    def test_right_shift(self):
        int1 = Int8(8)
        result = int1 >> 2
        self.assertEqual(result.value, 2)

    def test_comparison_operators(self):
        int1 = Int8(10)
        int2 = Int8(20)
        self.assertTrue(int1 < int2)
        self.assertTrue(int1 <= int2)
        self.assertTrue(int2 > int1)
        self.assertTrue(int2 >= int1)
        self.assertTrue(int1 != int2)
        self.assertTrue(int1 == Int8(10))

    def test_bitwise_invert_with_mask(self):
        int8 = Int8(10)
        result = ~int8
        self.assertEqual(result.value, -11 & 0xFF)

    def test_to_bits(self):
        int1 = Int8(10)
        self.assertEqual(int1.to_bits(), '0000000000001010')

    def test_to_pyint(self):
        int1 = Int8(10)
        self.assertEqual(int1.to_pyint(), 10)

    def test_hash(self):
        int1 = Int8(10)
        int2 = Int8(10)
        self.assertEqual(hash(int1), hash(int2))