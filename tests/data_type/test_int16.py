from unittest import TestCase
from src.data_type.int16 import Int16


class TestInt16(TestCase):

    def test_initialization(self):
        int16 = Int16(-2)
        self.assertEqual(int16.value, 0)

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

    def test_subtraction(self):
        int16_1 = Int16(30)
        int16_2 = Int16(20)
        result = int16_1 - int16_2
        self.assertEqual(result.value, 10)

    def test_multiplication(self):
        int16_1 = Int16(5)
        int16_2 = Int16(4)
        result = int16_1 * int16_2
        self.assertEqual(result.value, 20)

    def test_division(self):
        int16_1 = Int16(20)
        int16_2 = Int16(3)
        result = int16_1 / int16_2
        self.assertEqual(result.value, 6)

    def test_modulo(self):
        int16_1 = Int16(20)
        int16_2 = Int16(3)
        result = int16_1 % int16_2
        self.assertEqual(result.value, 2)

    def test_eq(self):
        int16_1 = Int16(10)
        int16_2 = Int16(10)
        self.assertTrue(int16_1 == int16_2)

    def test_ne(self):
        int16_1 = Int16(10)
        int16_2 = Int16(20)
        self.assertTrue(int16_1 != int16_2)

    def test_lt(self):
        int16_1 = Int16(10)
        int16_2 = Int16(20)
        self.assertTrue(int16_1 < int16_2)

    def test_gt(self):
        int16_1 = Int16(20)
        int16_2 = Int16(10)
        self.assertTrue(int16_1 > int16_2)

    def test_le(self):
        int16_1 = Int16(10)
        int16_2 = Int16(10)
        self.assertTrue(int16_1 <= int16_2)
        self.assertTrue(int16_1 <= Int16(20))

    def test_ge(self):
        int16_1 = Int16(20)
        int16_2 = Int16(10)
        self.assertTrue(int16_1 >= int16_2)
        self.assertTrue(int16_1 >= Int16(20))

    def test_and(self):
        int16_1 = Int16(0b1010)
        int16_2 = Int16(0b1100)
        result = int16_1 & int16_2
        self.assertEqual(result.value, 0b1000)

    def test_or(self):
        int16_1 = Int16(0b1010)
        int16_2 = Int16(0b1100)
        result = int16_1 | int16_2
        self.assertEqual(result.value, 0b1110)

    def test_xor(self):
        int16_1 = Int16(0b1010)
        int16_2 = Int16(0b1100)
        result = int16_1 ^ int16_2
        self.assertEqual(result.value, 0b0110)

    def test_invert(self):
        int16 = Int16(0b1010)
        result = ~int16
        self.assertEqual(result.value, -11 & 0xFFFF)

    def test_lshift(self):
        int16 = Int16(0b1010)
        result = int16 << Int16(2)
        self.assertEqual(result.value, 0b101000)

    def test_rshift(self):
        int16 = Int16(0b1010)
        result = int16 >> Int16(2)
        self.assertEqual(result.value, 0b10)

    def test_hash(self):
        int16_1 = Int16(10)
        int16_2 = Int16(10)
        self.assertEqual(hash(int16_1), hash(int16_2))

        int16_3 = Int16(20)
        self.assertNotEqual(hash(int16_1), hash(int16_3))

    def test_to_bits(self):
        int16 = Int16(10)
        self.assertEqual(int16.to_bits(), "0000000000001010")

    def test_to_pyint(self):
        int16 = Int16(10)
        self.assertEqual(int16.to_pyint(), 10)
