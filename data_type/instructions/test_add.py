from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import Add, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestAdd(TestCase):
    def test_add_register_to_register(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()


        cpu.get_register_val.side_effect = lambda reg: Int16(100) if reg == Register.eax else Int16(50)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        add_instruction = Add(Operand(Register.eax), Operand(Register.ebx))

        add_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(150))




