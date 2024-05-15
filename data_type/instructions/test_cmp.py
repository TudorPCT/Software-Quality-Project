from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import Cmp, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestCmp(TestCase):
    def test_cmp_registers(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.get_register_val.side_effect = lambda reg: Int16(10) if reg == Register.eax else Int16(10)
        cpu.register_ip = Int16()

        cpu.flag_eq = False
        cpu.flag_neq = False
        cpu.flag_lt = False
        cpu.flag_gt = False

        cmp_instruction = Cmp(Operand(Register.eax), Operand(Register.ebx))

        cmp_instruction.run(cpu)

        self.assertTrue(cpu.flag_eq)
        self.assertFalse(cpu.flag_neq)
        self.assertFalse(cpu.flag_lt)  #lt=less than
        self.assertFalse(cpu.flag_gt) #gt=greater than
