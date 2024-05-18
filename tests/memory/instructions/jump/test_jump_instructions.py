from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.flag import Flag
from src.data_type.int16 import Int16
from src.memory.instructions.jump_instructions import Jmp, JEQ
from src.processor.processor import Operand


class TestJmp(TestCase):
    def test_condition(self):
        address = Operand(Int16(42))
        cpu = MagicMock()
        jmp_instruction = Jmp(address)

        self.assertTrue(jmp_instruction.condition(cpu))


class TestJEQ(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock()
        cpu.flag_eq = Flag(True)
        jeq_instruction = JEQ(address)

        result = jeq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertTrue(jeq_instruction.condition(cpu).to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock()
        cpu.flag_eq = Flag(False)
        jeq_instruction = JEQ(address)

        result = jeq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())


