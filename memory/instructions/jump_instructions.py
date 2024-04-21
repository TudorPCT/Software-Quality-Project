from memory.instructions.instruction import Instruction, Processor, Operand, MemoryLocation, Register, Int16, Flag, get_value, set_value


class BasicJumpInstruction(Instruction):
    def __init__(self, address: Operand):
        super().__init__()
        assert isinstance(address.data, Int16)
        self.address = address.data

    def run(self, cpu: Processor) -> None:
        if self.condition(cpu):
            cpu.register_ip = self.address
        else:
            self.end(cpu)

    def condition(self, cpu: Processor) -> Flag:
        raise NotImplementedError()


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