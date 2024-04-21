from memory.instructions.instruction import Instruction, Processor, Operand, MemoryLocation, Register, Int16, get_value, set_value


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
        cpu.register_esp -= 2

        assert cpu.register_esp > 0, "Stack Overflow!"


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
        assert cpu.main_memory.get_stack_base() >= cpu.register_esp + 2

        set_value(cpu, location, cpu.main_memory[cpu.register_esp + 2])
        cpu.register_esp += 2


class Call(Instruction):
    """
    pop eax
    """

    def __init__(self, address: Operand):
        super().__init__()
        self.address = address

    def run(self, cpu: Processor) -> None:
        pass


class Ret(Instruction):
    """
    ret
    """

    def __init__(self):
        super().__init__()

    def run(self, cpu: Processor) -> None:
        Pop.static_run(Operand(Register.ip), cpu)


