from data_type.int16 import Int16
from processor.processor import Operand, Processor, Register, MemoryLocation


def get_value(cpu: Processor, op: Operand) -> Int16():
    if isinstance(op.data, Int16):
        return op.data

    if isinstance(op.data, Register):
        return cpu.get_register_val(op.data)

    if isinstance(op.data, MemoryLocation):
        return cpu.main_memory[get_value(cpu, Operand(op.data.data))]


def set_value(cpu: Processor, op: Operand, val: Int16()) -> None:
    assert not isinstance(op.data, Int16)

    if isinstance(op.data, Register):
        cpu.set_register_val(op.data, val)

    if isinstance(op.data, MemoryLocation):
        cpu.main_memory[get_value(cpu, Operand(op.data.data))] = val


class Instruction:
    def __init__(self):
        pass

    def run(self, cpu: Processor) -> None:
        raise NotImplementedError()

    def end(self, cpu: Processor):
        cpu.register_ip += Int16(1)

