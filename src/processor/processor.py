from src.data_type.int16 import Int16
from src.data_type.flag import Flag
from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.memory.program_memory import ProgramMemory

from src.memory.main_memory import MainMemory
from enum import Enum


class Register(Enum):
    eax = 0
    ebx = 1
    ecx = 2
    edx = 3
    efx = 4
    register_ebp_egx = 5
    ip = 6
    esp = 7


class MemoryLocation:
    def __init__(self, data: Register | Int16):
        self.data = data

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.data == other.data

    def __hash__(self):
        return hash(self.data)


class Operand:
    def __init__(self, data: Int16 | Register | MemoryLocation):
        self.data = data

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.data == other.data


class KillSwitch:
    def __init__(self):
        self.kill = False


class Processor:
    def __init__(self, main_memory: MainMemory, program_memory: 'ProgramMemory'):
        self.register_eax = Int16()
        self.register_ebx = Int16()
        self.register_ecx = Int16()
        self.register_edx = Int16()
        self.register_efx = Int16()
        self.register_ebp_egx = Int16()
        self.register_ip = Int16()
        self.register_esp = main_memory.get_stack_base()
        self.__stack_information(self.register_esp)

        self.flag_eq = Flag(False)
        self.flag_neq = Flag(False)
        self.flag_lt = Flag(False)
        self.flag_gt = Flag(False)
        self.flag_lteq = Flag(False)
        self.flag_gteq = Flag(False)

        self.flag_zero = Flag(False)

        self.main_memory = main_memory
        self.program_memory = program_memory

    @staticmethod
    def __stack_information(stack_base: Int16):
        print(f"Stack starts from {stack_base} and continues downwards")

    def reset_flags(self):
        self.flag_eq = Flag(False)
        self.flag_neq = Flag(False)
        self.flag_lt = Flag(False)
        self.flag_gt = Flag(False)
        self.flag_lteq = Flag(False)
        self.flag_gteq = Flag(False)

    def reset_arithemetic_flags(self):
        self.flag_zero = Flag(False)

    def get_register_val(self, register: Register) -> Int16:
        return getattr(self, f"register_{register.name}")

    def set_register_val(self, register: Register, val: Int16):
        setattr(self, f"register_{register.name}", val)

    def run(self, kill_switch: Optional[KillSwitch] = None):
        while self.register_ip < self.program_memory.get_len():

            if kill_switch is not None and kill_switch.kill is True:
                break

            current_instruction = self.program_memory[self.register_ip]
            current_instruction.run(self)



