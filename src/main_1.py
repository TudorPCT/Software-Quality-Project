from memory.main_memory import MainMemory
from memory.program_memory import ProgramMemory
from processor.processor import Processor
from processor.read_instructions import InstructionParser
from pathlib import Path
import os

RES_DIR = os.path.join(str(Path(__file__).parent.absolute()), "resources")

if __name__ == "__main__":
    # instruction_parser = InstructionParser(r"D:\personal\Quality\Software-Quality-Project\resources\instructions.txt")
    instruction_parser = InstructionParser(
        os.path.join(RES_DIR, "instructions_prim.txt")
    )

    instructions = instruction_parser.read_instructions_from_file()

    main_memory = MainMemory(1024, [])
    program_memory = ProgramMemory(1024)
    program_memory.load_program(instructions)

    cpu = Processor(main_memory, program_memory)
    cpu.run()

    # print(cpu.register_ebx)
    print(cpu.register_edx)
