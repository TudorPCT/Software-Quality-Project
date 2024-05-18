from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.flag import Flag
from src.data_type.int16 import Int16
from src.memory.instructions.jump_instructions import Jmp, JEQ, JNEQ, JGT, JLT, JGTEQ, JLTEQ, JZ, JNZ
from src.processor.processor import Operand, Processor


class TestJmp(TestCase):
    def test_condition(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        jmp_instruction = Jmp(address)

        self.assertTrue(jmp_instruction.condition(cpu))


class TestJEQ(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_eq = Flag(True)
        jeq_instruction = JEQ(address)

        result = jeq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertTrue(jeq_instruction.condition(cpu).to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_eq = Flag(False)
        jeq_instruction = JEQ(address)

        result = jeq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())


class TestJNEQ(TestCase):
    
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_neq = Flag(True)
        jne_instruction = JNEQ(address)

        result = jne_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_neq = Flag(False)
        jne_instruction = JNEQ(address)

        result = jne_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())


class TestJGT(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_gt = Flag(True)
        jgt_instruction = JGT(address)

        result = jgt_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertTrue(result.to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_gt = Flag(False)
        jgt_instruction = JGT(address)

        result = jgt_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())

        
class TestJLT(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_lt = Flag(True)
        jlt_instruction = JLT(address)

        result = jlt_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertTrue(result.to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_lt = Flag(False)
        jlt_instruction = JLT(address)

        result = jlt_instruction.condition(cpu)
        
        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())


class TestJGTEQ(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_gteq = Flag(True)
        jgteq_instruction = JGTEQ(address)

        result = jgteq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertTrue(result.to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_gteq = Flag(False)
        jgteq_instruction = JGTEQ(address)

        result = jgteq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())


class TestJLTEQ(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_lteq = Flag(True)
        jlteq_instruction = JLTEQ(address)

        result = jlteq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertTrue(result.to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_lteq = Flag(False)
        jlteq_instruction = JLTEQ(address)

        result = jlteq_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())


class TestJZ(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_zero = Flag(True)
        jz_instruction = JZ(address)

        result = jz_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertTrue(result.to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_zero = Flag(False)
        jz_instruction = JZ(address)

        result = jz_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())


class TestJNZ(TestCase):
    def test_condition_true(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_zero = Flag(False)
        jnz_instruction = JNZ(address)

        result = jnz_instruction.condition(cpu)
        self.assertIsInstance(result, Flag)
        self.assertTrue(result.to_pybool())

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.flag_zero = Flag(True)
        jnz_instruction = JNZ(address)

        result = jnz_instruction.condition(cpu)

        self.assertIsInstance(result, Flag)
        self.assertFalse(result.to_pybool())
