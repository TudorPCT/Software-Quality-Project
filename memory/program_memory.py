from data_type.int16 import Int16
from data_type.flag import Flag
from processor.processor import Operand, Processor, Register, MemoryLocation
from memory.instructions.instruction import Instruction


class ProgramMemory:
    def __init__(self, size: int):
        self.__size = size
        self.__instructions = list[Instruction]()

    def load_program(self, program: list[Instruction]):
        assert len(program) < self.__size
        self.__instructions = program

    def __getitem__(self, idx: Int16) -> Instruction:
        return self.__instructions[idx.to_pyint()]

    def get_len(self) -> Int16:
        return Int16(len(self.__instructions))
