from unittest import TestCase

from src.data_type.flag import Flag


class TestFlag(TestCase):

    def test_initialization(self):
        flag = Flag()
        self.assertIsInstance(flag, Flag)
        self.assertFalse(flag.value)

        flag = Flag(True)
        self.assertTrue(flag.value)

    def test_to_pybool(self):
        flag = Flag()
        self.assertEqual(flag.to_pybool(), False)

        flag = Flag(True)
        self.assertEqual(flag.to_pybool(), True)

    def test_bitwise_or(self):
        flag1 = Flag()
        flag2 = Flag()
        result = flag1 | flag2
        self.assertIsInstance(result, Flag)
        self.assertFalse(result.value)

        flag1 = Flag(True)
        flag2 = Flag()
        result = flag1 | flag2
        self.assertTrue(result.value)

        flag1 = Flag()
        flag2 = Flag(True)
        result = flag1 | flag2
        self.assertTrue(result.value)

        flag1 = Flag(True)
        flag2 = Flag(True)
        result = flag1 | flag2
        self.assertTrue(result.value)

    def test_logical_negation(self):
        flag = Flag()
        result = flag.__not__()
        self.assertIsInstance(result, Flag)
        self.assertTrue(result.value)

        flag = Flag(True)
        result = flag.__not__()
        self.assertFalse(result.value)
