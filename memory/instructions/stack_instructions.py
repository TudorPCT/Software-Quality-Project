from memory.instructions.instruction import Instruction, Processor, Operand, MemoryLocation, Register, Int16, get_value, set_value


class Push(Instruction):
    """
    push eax
    """

    def __init__(self, location: Operand):
        super().__init__()
        self.location = location

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

class Pop(Instruction):
    """
    pop eax
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class Call(Instruction):
    """
    pop eax
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh


class Ret(Instruction):
    """
    pop eax
    """

    def __init__(self, lh: Operand):
        super().__init__()
        self.lh = lh
