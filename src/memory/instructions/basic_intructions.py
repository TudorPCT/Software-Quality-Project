<<<<<<< HEAD:src/memory/instructions/basic_intructions.py
from src.memory.instructions.instruction import Instruction, Processor, Operand, MemoryLocation, Register, Int16, get_value, set_value
=======
from memory.instructions.instruction import Instruction, Processor, Operand, \
    MemoryLocation, Register, Int16, get_value, set_value
>>>>>>> main:memory/instructions/basic_intructions.py


class BasicInstruction(Instruction):
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh

    def run(self, cpu: Processor) -> None:
        assert isinstance(self.lh.data, Register) or isinstance(self.lh.data, MemoryLocation)

        zero = Int16(0)

        cpu.reset_arithemetic_flags()

        lh_val = get_value(cpu, self.lh)
        rh_val = get_value(cpu, self.rh)

        result = self.operation(lh_val, rh_val)

        cpu.flag_zero = result == zero

        set_value(cpu, self.lh, result)

        self.end(cpu)

    def operation(self, lh: Int16, rh: Int16) -> Int16:
        raise NotImplementedError()


class Mov(Instruction):
    """
    mov eax, ebx
    mov eax, 10
    mov [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh

    def run(self, cpu: Processor) -> None:
        assert isinstance(self.lh.data, Register) or isinstance(self.lh.data, MemoryLocation)
        rh_val = get_value(cpu, self.rh)
        set_value(cpu, self.lh, rh_val)
        self.end(cpu)


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


class Mul(Instruction):
    """
    mul ebx
    mul 10
    mul [10]
    """

    def __init__(self, rh: Operand):
        super().__init__()
        self.rh = rh

    def run(self, cpu: Processor) -> None:
        result = cpu.register_eax * self.rh.data

        set_value(cpu, Operand(Register["eax"]), result)

        self.end(cpu)


class Div(Instruction):
    """
    div ebx
    div 10
    div [10]
    """

    def __init__(self, rh: Operand):
        super().__init__()
        self.rh = rh

    def run(self, cpu: Processor) -> None:
        result = cpu.register_eax / self.rh.data
        remainder = cpu.register_eax % self.rh.data

        set_value(cpu, Operand(Register["eax"]), result)
        set_value(cpu, Operand(Register["edx"]), remainder)

        self.end(cpu)


class NOT(Instruction):
    """
    not eax
    not eax
    """
    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh

    def run(self, cpu: Processor) -> None:
        lh_val = get_value(cpu, self.lh)
        set_value(cpu, self.lh, ~lh_val)
        self.end(cpu)


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
        self.end(cpu)
