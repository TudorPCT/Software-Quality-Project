from data_type.int16 import Int16
from data_type.int8 import Int8
from memory.program_memory import ProgramMemory
from memory.main_memory import MainMemory
from enum import Enum



class Registries(Enum):
    eax = 0
    ebx = 1
    ecx = 2
    edx = 3
    efx = 4
    egx = 5
    ip = 6
    esp = 7


class MemoryLocation:
    def __init__(self, data: Registries | Int16):
        self.data = data


class Operand:
    def __init__(self, data: Int16 | Registries | MemoryLocation):
        self.data = data



class Processor:
    def __init__(self, main_memory: MainMemory, program_memory: ProgramMemory):
        self.eax = Int16()
        self.ebx = Int16()
        self.ecx = Int16()
        self.edx = Int16()
        self.efx = Int16()
        self.egx = Int16()
        self.ip = Int16()
        self.esp = Int16()

        self.main_memory = main_memory
        self.program_memory = program_memory

    def run(self):
        while self.ip < len(self.program_memory):
            current_instruction = self.program_memory[self.ip]
            current_instruction.run(self)
