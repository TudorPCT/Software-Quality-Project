from memory.instructions.instruction import Instruction, Processor, Operand, MemoryLocation, Register, Int16, get_value, set_value


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
