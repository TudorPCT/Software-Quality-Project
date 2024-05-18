from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.instruction import Operand, Int16
from memory.instructions.jump_instructions import Jmp
from processor.processor import Processor

class TestJmp(TestCase):
    def test_jmp(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.register_ip = Int16()
        cpu.flag_some_condition = True

        address_operand = Operand(Int16(24))

        jmp_instruction = Jmp(address_operand)

        jmp_instruction.run(cpu)
