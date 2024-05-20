import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.data_type.int16 import Int16
from src.processor.processor import Processor, Operand


class TestCall(TestCase):

    def setUp(self):
        if 'src.memory.instructions.stack_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.stack_instructions']

    @patch('src.memory.instructions.stack_instructions.Push.static_run')
    @patch('src.memory.instructions.stack_instructions.BasicJumpInstruction.static_run')
    def test_call(self, mock_basic_jump_static_run, mock_push_static_run):
        from src.memory.instructions.stack_instructions import Call

        cpu = MagicMock(Processor)
        cpu.register_ip = Int16(10)

        address_operand = Operand(Int16(100))

        call_instruction = Call(address_operand)

        call_instruction.run(cpu)

        mock_push_static_run.assert_called_once_with(Operand(cpu.register_ip + Int16(1)), cpu)

        mock_basic_jump_static_run.assert_called_once_with(address_operand, cpu)
