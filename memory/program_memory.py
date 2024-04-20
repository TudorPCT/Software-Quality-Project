from data_type.int16 import Int16
from data_type.flag import Flag
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


class BasicInstruction(Instruction):
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh

    def run(self, cpu: Processor) -> None:
        assert isinstance(self.lh.data, Register) or isinstance(self.lh.data, MemoryLocation)
        lh_val = get_value(cpu, self.lh)
        rh_val = get_value(cpu, self.rh)
        set_value(cpu, self.lh, self.operation(lh_val, rh_val))
        self.end(cpu)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        raise NotImplementedError()


class BasicJumpInstruction(Instruction):
    def __init__(self, address: Operand):
        super().__init__()
        assert isinstance(address.data, Int16)
        self.address = address

    def run(self, cpu: Processor) -> None:
        if self.condition(cpu):
            cpu.register_ip = self.address
        else:
            self.end(cpu)

    def condition(self, cpu: Processor) -> Flag:
        raise NotImplementedError()


class Mov(BasicInstruction):
    """
    mov eax, ebx
    mov eax, 10
    mov [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return rh


class Add(BasicInstruction):
    """
    add eax, ebx
    add eax, 10
    add [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh + rh


class Sub(BasicInstruction):
    """
    sub eax, ebx
    sub eax, 10
    sub [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh - rh


class Mul(BasicInstruction):
    """
    mul eax, ebx
    mul eax, 10
    mul [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh * rh


class Div(BasicInstruction):
    """
    div eax, ebx
    div eax, 10
    div [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh / rh


class NOT(Instruction):
    """
    not eax
    not eax
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class AND(BasicInstruction):
    """
    and eax, ebx
    and eax, 10
    and [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh & rh


class OR(BasicInstruction):
    """
    or eax, ebx
    or eax, 10
    or [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh | rh


class XOR(BasicInstruction):
    """
    xor eax, ebx
    xor eax, 10
    xor [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh ^ rh


class SHL(BasicInstruction):
    """
    shl eax, ebx
    shl eax, 10
    shl [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh << rh


class SHR(BasicInstruction):
    """
    shr eax, ebx
    shr eax, 10
    shr [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__(lh, rh)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        return lh >> rh


class Cmp(Instruction):
    """
    cmp eax, ebx
    cmp eax, 10
    cmp [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh

    def run(self, cpu: Processor) -> None:
        lh_val = get_value(cpu, self.lh)
        rh_val = get_value(cpu, self.rh)

        cpu.reset_flags()

        cpu.flag_eq = lh_val == rh_val
        cpu.flag_neq = lh_val != rh_val
        cpu.flag_lt = lh_val < rh_val
        cpu.flag_gt = lh_val > rh_val

        cpu.flag_lteq = cpu.flag_eq or cpu.flag_lt
        cpu.flag_gteq = cpu.flag_eq or cpu.flag_gt


class Jmp(BasicJumpInstruction):
    """
    jmp functie1
    jmp 24
    """
    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> Flag:
        return Flag(True)


class JEQ(BasicJumpInstruction):
    """
    jme functie1
    """
    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> Flag:
        return cpu.flag_eq


class JNEQ(BasicJumpInstruction):
    """
    jme functie1
    """
    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> Flag:
        return cpu.flag_neq


class JGT(BasicJumpInstruction):
    """
    jme functie1
    """

    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> Flag:
        return cpu.flag_gt


class JLT(BasicJumpInstruction):
    """
    jme functie1
    """

    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> Flag:
        return cpu.flag_lt


class JGTEQ(BasicJumpInstruction):
    """
    jme functie1
    """

    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> Flag:
        return cpu.flag_gteq


class JLTEQ(BasicJumpInstruction):
    """
    jme functie1
    """

    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> Flag:
        return cpu.flag_lteq


class Push(Instruction):
    """
    push eax
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh

class Pop(Instruction):
    """
    pop eax
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class ProgramMemory:
    def __init__(self, size: int):
        self.size = size
        self.__instructions = list[Instruction]()

    def load_program(self, program: list[Instruction]):
        assert len(program) < self.size
        self.__instructions = program

    def __getitem__(self, idx: Int16) -> Instruction:
        return self.__instructions[idx.to_pyint()]

    def get_len(self) -> Int16:
        return Int16(len(self.__instructions))
