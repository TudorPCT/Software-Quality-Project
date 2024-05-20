import unittest
from unittest import TestCase

from src.data_type.flag import Flag


class TestFlag(TestCase):

    def test_initialization(self):
        flag1 = Flag()
        self.assertEqual(flag1.value, False)

        flag2 = Flag(True)
        self.assertEqual(flag2.value, True)

    def test_to_pybool(self):
        flag1 = Flag()
        self.assertEqual(flag1.to_pybool(), False)

        flag2 = Flag(True)
        self.assertEqual(flag2.to_pybool(), True)

    def test_or_operator(self):
        flag1 = Flag()
        flag2 = Flag(True)
        result1 = flag1 | flag2
        self.assertEqual(result1.value, True)

        result2 = flag1 | Flag()
        self.assertEqual(result2.value, False)

    def test_hash(self):
        flag1 = Flag()
        flag2 = Flag()
        self.assertEqual(hash(flag1), hash(flag2))

        flag3 = Flag(True)
        self.assertNotEqual(hash(flag1), hash(flag3))

    def test_not_operator(self):
        flag1 = Flag()
        result1 = flag1.__not__()
        self.assertEqual(result1.value, True)

        flag2 = Flag(True)
        result2 = flag2.__not__()
        self.assertEqual(result2.value, False)
