from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import Div, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestDiv(TestCase):
    def test_div_register_by_register(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.get_register_val.side_effect = lambda reg: Int16(30) if reg == Register.eax else Int16(6)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        div_instruction = Div(Operand(Register.eax), Operand(Register.ebx))

        div_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(5))

    def test_div_by_zero(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()


        cpu.get_register_val.side_effect = lambda reg: Int16(100) if reg == Register.eax else Int16(0)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        div_instruction = Div(Operand(Register.eax), Operand(Register.ebx))

        with self.assertRaises(ZeroDivisionError):
            div_instruction.run(cpu)
