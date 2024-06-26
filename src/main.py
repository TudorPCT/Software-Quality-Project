from memory.main_memory import MainMemory
from memory.program_memory import ProgramMemory
from memory.instructions.basic_instructions import *
from memory.instructions.stack_instructions import *
from processor.processor import Processor


def main():
    program = [
        Mov(Operand(Register.eax), Operand(Int16(24))),
        Add(Operand(Register.eax), Operand(Int16(14)))
    ]

    main_memory = MainMemory(1024, [])
    program_memory = ProgramMemory(1024)
    program_memory.load_program(program)

    cpu = Processor(main_memory, program_memory)
    cpu.run()

    print(cpu.register_eax)


if __name__ == "__main__":
    main()
