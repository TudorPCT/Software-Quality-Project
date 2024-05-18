from src.data_type.int8 import Int8
from src.data_type.int16 import Int16
from unittest.mock import MagicMock, Mock
from src.memory.instructions.basic_intructions import Mov, Add
from src.processor.processor import Register, Operand
import unittest
import os
from src.memory.program_memory import ProgramMemory
from pathlib import Path


RES_DIR = os.path.join(str(Path(__file__).parent.absolute()), "../resources")


class TestProgramMemory(unittest.TestCase):

    def test_memory_size_arg(self):
        self.assertRaises(AssertionError, lambda: ProgramMemory(500))
        ProgramMemory(1024)
        ProgramMemory(2048)
        self.assertRaises(AssertionError, lambda: ProgramMemory(3000))
        self.assertRaises(AssertionError, lambda: ProgramMemory(131072))

    def test_memory_load_get_len(self):
        program = [
            Mov(Operand(Register.eax), Operand(Int16(24))),
            Add(Operand(Register.eax), Operand(Int16(14)))
        ]

        memory = ProgramMemory(1024)
        memory.load_program(program)
        self.assertTrue(memory.get_len() == Int16(2))
        instruction = memory[Int16(1)]

        self.assertTrue(instruction == program[1])
