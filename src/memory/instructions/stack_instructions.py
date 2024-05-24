from src.memory.instructions.instruction import Instruction, Processor, Operand, MemoryLocation, \
    Register, Int16, get_value, set_value
from src.memory.instructions.jump_instructions import BasicJumpInstruction


class Push(Instruction):
    """
    push eax
    """

    def __init__(self, location: Operand):
        super().__init__()
        self.location = location

    def run(self, cpu: Processor) -> None:
        self.static_run(self.location, cpu)
        self.end(cpu)

    @staticmethod
    def static_run(location: Operand, cpu: Processor):
        cpu.main_memory[cpu.register_esp] = get_value(cpu, location)
        cpu.register_esp -= Int16(2)

        assert cpu.register_esp > Int16(0), "Stack Overflow!"


class Pop(Instruction):
    """
    pop eax
    """

    def __init__(self, location: Operand):
        super().__init__()
        self.location = location

    def run(self, cpu: Processor) -> None:
        self.static_run(self.location, cpu)
        self.end(cpu)

    @staticmethod
    def static_run(location: Operand, cpu: Processor):
        assert isinstance(location.data, Register) or isinstance(location.data, MemoryLocation)
        assert cpu.main_memory.get_stack_base() >= cpu.register_esp + Int16(2)

        set_value(cpu, location, cpu.main_memory[cpu.register_esp + Int16(2)])
        cpu.register_esp += Int16(2)
        assert cpu.main_memory.get_stack_base() >= cpu.register_esp


class Call(Instruction):
    """
    pop eax
    """

    def __init__(self, address: Operand):
        super().__init__()
        self.address = address

    def run(self, cpu: Processor) -> None:
        Push.static_run(Operand(cpu.register_ip + Int16(1)), cpu)
        BasicJumpInstruction.static_run(self.address, cpu)


class Ret(Instruction):
    """
    ret
    """

    def __init__(self):
        super().__init__()

    def run(self, cpu: Processor) -> None:
        Pop.static_run(Operand(Register.ip), cpu)
