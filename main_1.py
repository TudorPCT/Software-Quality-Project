from memory.main_memory import MainMemory
from memory.program_memory import ProgramMemory, Operand, Int16, MemoryLocation, Add, Mov, Register
from processor.processor import Processor
from processor.read_instructions import InstructionParser


if __name__ == "__main__":
    instruction_parser = InstructionParser(r"D:\personal\Quality\Software-Quality-Project\resources\instructions.txt")
    instructions = instruction_parser.read_instructions_from_file()

    main_memory = MainMemory(128)
    program_memory = ProgramMemory(128)
    program_memory.load_program(instructions)

    cpu = Processor(main_memory, program_memory)
    cpu.run()

    print(cpu.register_ebx)

