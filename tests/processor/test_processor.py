from unittest.mock import MagicMock, Mock
import unittest
import os
from src.data_type.int16 import Int16
from src.data_type.flag import Flag
from src.processor.processor import Processor, Register
from pathlib import Path


RES_DIR = os.path.join(str(Path(__file__).parent.absolute()), "../resources")


def util_mock_run(processor_arg: Processor):
    processor_arg.set_register_val(Register.ip, processor_arg.get_register_val(Register.ip) + Int16(1))


class TestProcessor(unittest.TestCase):

    def test_cpu_running(self):
        memory_mock = Mock()
        memory_mock.get_stack_base = Mock(return_value=Int16(128))

        program_memory_mock = Mock()
        program_memory_mock.get_len = Mock(return_value=Int16(3))

        program_instruction_mock = Mock()
        program_instruction_mock.run = Mock()
        program_instruction_mock.run.side_effect = util_mock_run

        program_memory_mock.__getitem__ = Mock(return_value=program_instruction_mock)

        cpu = Processor(memory_mock, program_memory_mock)
        cpu.run()

        self.assertTrue(program_instruction_mock.run.call_count == 3)
        self.assertTrue(cpu.register_ip == Int16(3))

    def test_cpu_registers(self):
        memory_mock = Mock()
        memory_mock.get_stack_base = Mock(return_value=Int16(128))

        program_memory_mock = Mock()
        program_memory_mock.get_len = Mock(return_value=Int16(3))

        cpu = Processor(memory_mock, program_memory_mock)

        for it, reg in enumerate(Register):
            cpu.set_register_val(reg, Int16(it))

        for it, reg in enumerate(Register):
            self.assertTrue(cpu.get_register_val(reg) == Int16(it))

    def test_cpu_flags(self):
        memory_mock = Mock()
        memory_mock.get_stack_base = Mock(return_value=Int16(128))

        program_memory_mock = Mock()
        program_memory_mock.get_len = Mock(return_value=Int16(3))

        cpu = Processor(memory_mock, program_memory_mock)
        cpu.flag_lt = Flag(True)
        cpu.flag_gt = Flag(True)
        cpu.flag_zero = Flag(True)

        cpu.reset_flags()
        self.assertTrue(cpu.flag_lt.value == Flag(False).value)
        self.assertTrue(cpu.flag_gt.value == Flag(False).value)
        self.assertTrue(cpu.flag_zero.value == Flag(True).value)

        cpu.reset_arithemetic_flags()
        self.assertTrue(cpu.flag_zero.value == Flag(False).value)


if __name__ == '__main__':
    unittest.main()
