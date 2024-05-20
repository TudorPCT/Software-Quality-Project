import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.processor.processor import Processor, Operand, Register


class TestRet(TestCase):

    def setUp(self):
        if 'src.memory.instructions.stack_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.stack_instructions']

    @patch('src.memory.instructions.stack_instructions.Pop.static_run')
    def test_ret(self, mock_pop_static_run):
        from src.memory.instructions.stack_instructions import Ret

        cpu = MagicMock(Processor)

        ret_instruction = Ret()

        ret_instruction.run(cpu)

        mock_pop_static_run.assert_called_once_with(Operand(Register.ip), cpu)
