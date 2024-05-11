from unittest import TestCase

from src.processor.processor import Operand, Register


class TestAdd(TestCase):

    def test_operation(self):
        eax = Operand(Register["eax"])
        self.fail()
