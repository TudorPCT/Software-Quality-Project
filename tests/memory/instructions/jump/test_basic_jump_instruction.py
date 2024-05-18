from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.jump_instructions import BasicJumpInstruction
from src.processor.processor import Operand, Processor


class TestBasicJumpInstruction(TestCase):

    def test_condition_true(self):
        address = Operand(Int16(42))

        cpu = MagicMock(Processor)

        instruction = BasicJumpInstruction(address=address)
        instruction.condition = MagicMock(return_value=True)

        instruction.run(cpu)
        self.assertEqual(cpu.register_ip, Int16(42))

    def test_condition_false(self):
        address = Operand(Int16(42))
        cpu = MagicMock(Processor)
        cpu.register_ip = Int16(0)
        instruction = BasicJumpInstruction(address=address)
        instruction.condition = MagicMock(return_value=False)

        instruction.run(cpu)
        self.assertNotEqual(cpu.register_ip, Int16(42))

    def test_static_run(self):
        address = Operand(Int16(24))
        cpu = MagicMock(Processor)

        BasicJumpInstruction.static_run(address, cpu)
        self.assertEqual(cpu.register_ip, Int16(24))
