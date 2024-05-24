from src.data_type.int16 import Int16
from src.processor.processor import Operand, Processor, Register, MemoryLocation


def get_value(cpu: Processor, op: Operand) -> Int16:
    assert isinstance(op, Operand)
    result = None

    if isinstance(op.data, Int16):
        result = op.data
    elif isinstance(op.data, Register):
        result = cpu.get_register_val(op.data)
    elif isinstance(op.data, MemoryLocation):
        result = cpu.main_memory[get_value(cpu, Operand(op.data.data))]

    assert isinstance(result, Int16)
    return result


def set_value(cpu: Processor, op: Operand, val: Int16) -> None:
    assert not isinstance(op.data, Int16)

    if isinstance(op.data, Register):
        cpu.set_register_val(op.data, val)

    if isinstance(op.data, MemoryLocation):
        cpu.main_memory[get_value(cpu, Operand(op.data.data))] = val

    assert get_value(cpu, op) == val


class Instruction:
    def __init__(self):
        pass

    def run(self, cpu: Processor) -> None:
        raise NotImplementedError()

    def end(self, cpu: Processor):
        cpu.register_ip += Int16(1)
