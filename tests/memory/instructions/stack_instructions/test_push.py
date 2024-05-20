import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch
from src.data_type.int16 import Int16
from src.processor.processor import Processor, Operand, Register


class TestPush(TestCase):

    def setUp(self):
        if 'src.memory.instructions.stack_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.stack_instructions']

    @patch('src.memory.instructions.instruction.get_value')
    def test_push_register(self, mock_get_value):
        from src.memory.instructions.stack_instructions import Push

        cpu = MagicMock(Processor)
        cpu.register_esp = Int16(1024)
        cpu.main_memory = MagicMock()
        cpu.register_ip = Int16(0)

        mock_get_value.return_value = Int16(42)

        push_instruction = Push(Operand(Register.eax))

        push_instruction.run(cpu)

        mock_get_value.assert_called_once_with(cpu, Operand(Register.eax))
        cpu.main_memory.__setitem__.assert_called_once_with(Int16(1024), Int16(42))
        self.assertEqual(cpu.register_esp, Int16(1022))

    @patch('src.memory.instructions.instruction.get_value')
    def test_push_memory_location(self, mock_get_value):
        from src.memory.instructions.stack_instructions import Push

        cpu = MagicMock(Processor)
        cpu.register_esp = Int16(1024)
        cpu.main_memory = MagicMock()
        cpu.register_ip = Int16(0)

        mock_get_value.return_value = Int16(84)

        push_instruction = Push(Operand(Int16(500)))

        push_instruction.run(cpu)

        mock_get_value.assert_called_once_with(cpu, Operand(Int16(500)))
        cpu.main_memory.__setitem__.assert_called_once_with(Int16(1024), Int16(84))
        self.assertEqual(cpu.register_esp, Int16(1022))

    @patch('src.memory.instructions.instruction.get_value')
    def test_stack_overflow(self, mock_get_value):
        from src.memory.instructions.stack_instructions import Push

        cpu = MagicMock(Processor)
        cpu.register_esp = Int16(1)
        cpu.main_memory = MagicMock()
        cpu.register_ip = Int16(0)

        mock_get_value.return_value = Int16(42)

        push_instruction = Push(Operand(Register.eax))

        with self.assertRaises(AssertionError, msg="Stack Overflow!"):
            push_instruction.run(cpu)
