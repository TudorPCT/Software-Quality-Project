from data_type.flag import Flag
from memory.instructions.instruction import Instruction, Processor, Operand, Int16


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

    @staticmethod
    def static_run(address: Operand, cpu: Processor):
        assert isinstance(address.data, Int16)
        cpu.register_ip = address.data

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


class JZ(BasicJumpInstruction):
    """
    jz label
    """

    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> bool:
        return cpu.flag_zero


class JNZ(BasicJumpInstruction):
    """
    jnz label
    """

    def __init__(self, address: Operand):
        super().__init__(address)

    def condition(self, cpu: Processor) -> bool:
        return not cpu.flag_zero
