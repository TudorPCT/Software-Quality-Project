from data_type.int16 import Int16
from data_type.int8 import Int8
from data_type.flag import Flag

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from memory.program_memory import ProgramMemory

from memory.main_memory import MainMemory
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


class Operand:
    def __init__(self, data: Int16 | Register | MemoryLocation):
        self.data = data


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

        self.flag_zero = False
        self.flag_carry = False
        self.flag_overflow = False
        self.flag_negative = False

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
        self.flag_zero = False
        self.flag_carry = False
        self.flag_overflow = False
        self.flag_negative = False

    def get_register_val(self, register: Register) -> Int16:
        return getattr(self, f"register_{register.name}")

    def set_register_val(self, register: Register, val: Int16):
        setattr(self, f"register_{register.name}", val)

    def run(self):
        while self.register_ip < self.program_memory.get_len():
            current_instruction = self.program_memory[self.register_ip]
            current_instruction.run(self)
