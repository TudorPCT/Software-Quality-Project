from data_type.int16 import Int16
from processor.processor import Operand, Processor


class Instruction:
    def __init__(self):
        pass

    def run(self, cpu) -> None:
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
        raise NotImplementedError()


class Add(Instruction):
    """
    add eax, ebx
    add eax, 10
    add [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class Sub(Instruction):
    """
    sub eax, ebx
    sub eax, 10
    sub [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class Mul(Instruction):
    """
    mul eax, ebx
    mul eax, 10
    mul [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class Div(Instruction):
    """
    div eax, ebx
    div eax, 10
    div [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class NOT(Instruction):
    """
    not eax
    not eax
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh

class AND(Instruction):
    """
    and eax, ebx
    and eax, 10
    and [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class OR(Instruction):
    """
    or eax, ebx
    or eax, 10
    or [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class XOR(Instruction):
    """
    xor eax, ebx
    xor eax, 10
    xor [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class SHL(Instruction):
    """
    shl eax, ebx
    shl eax, 10
    shl [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


class SHR(Instruction):
    """
    shr eax, ebx
    shr eax, 10
    shr [10], ecx
    """
    def __init__(self, lh: Operand, rh: Operand):
        super().__init__()
        self.lh = lh
        self.rh = rh


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

class Jmp(Instruction):
    """
    jmp functie1
    jmp 24
    """
    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class JE(Instruction):
    """
    jme functie1
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class JNE(Instruction):
    """
    jme functie1
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh

class JZ(Instruction):
    """
    jme functie1
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class JG(Instruction):
    """
    jme functie1
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class JL(Instruction):
    """
    jme functie1
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class JGE(Instruction):
    """
    jme functie1
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class JLE(Instruction):
    """
    jme functie1
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh

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
    def __init__(self):
        self.__instructions = list[Instruction]()

    def __getitem__(self, idx: Int16) -> Instruction:
        return self.__instructions[idx.to_pyint()]

    def __len__(self) -> Int16:
        return Int16(len(self.__instructions))
