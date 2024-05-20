import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.data_type.int16 import Int16
from src.processor.processor import Processor, Operand, Register, MemoryLocation


class TestPop(TestCase):

    def setUp(self):
        if 'src.memory.instructions.stack_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.stack_instructions']

    @patch('src.memory.instructions.instruction.set_value')
    def test_pop_register(self, mock_set_value):
        from src.memory.instructions.stack_instructions import Pop

        cpu = MagicMock(Processor)
        cpu.register_esp = Int16(1022)
        cpu.main_memory = MagicMock()
        cpu.main_memory.__getitem__.return_value = Int16(42)
        cpu.main_memory.get_stack_base.return_value = Int16(2048)
        cpu.register_ip = Int16(0)

        pop_instruction = Pop(Operand(Register.eax))

        pop_instruction.run(cpu)

        mock_set_value.assert_called_once_with(cpu, Operand(Register.eax), Int16(42))
        cpu.main_memory.__getitem__.assert_called_once_with(Int16(1024))
        self.assertEqual(cpu.register_esp, Int16(1024))

    @patch('src.memory.instructions.instruction.set_value')
    def test_pop_memory_location(self, mock_set_value):
        from src.memory.instructions.stack_instructions import Pop

        cpu = MagicMock(Processor)
        cpu.register_esp = Int16(1022)
        cpu.main_memory = MagicMock()
        cpu.main_memory.__getitem__.return_value = Int16(84)
        cpu.main_memory.get_stack_base.return_value = Int16(2048)
        cpu.register_ip = Int16(0)

        pop_instruction = Pop(Operand(MemoryLocation(Int16(500))))

        pop_instruction.run(cpu)

        mock_set_value.assert_called_once_with(cpu, Operand(MemoryLocation(Int16(500))), Int16(84))
        cpu.main_memory.__getitem__.assert_called_once_with(Int16(1024))
        self.assertEqual(cpu.register_esp, Int16(1024))

    def test_stack_underflow(self):
        from src.memory.instructions.stack_instructions import Pop

        cpu = MagicMock(Processor)
        cpu.register_esp = Int16(2048)
        cpu.main_memory = MagicMock()
        cpu.main_memory.get_stack_base.return_value = Int16(2048)
        cpu.register_ip = Int16(0)

        pop_instruction = Pop(Operand(Register.eax))

        with self.assertRaises(AssertionError):
            pop_instruction.run(cpu)
