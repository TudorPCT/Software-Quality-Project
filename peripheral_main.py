from gui.computer_gui import ComputerGUI
from peripheral.keyboard_peripheral import KeyboardPeripheral
from peripheral.screen_peripheral import ScreenPeripheral
from memory.main_memory import MainMemory
from memory.program_memory import ProgramMemory
from processor.processor import Processor
from data_type.int8 import Int8
import time
from threading import Thread
from processor.read_instructions import InstructionParser


if __name__ == "__main__":
    #instruction_parser = InstructionParser(r"D:\personal\Quality\Software-Quality-Project\resources\instructions_prim.txt")
    instruction_parser = InstructionParser(r"D:\personal\Quality\Software-Quality-Project\resources\instructions_screen_keyboard.txt")
    instructions = instruction_parser.read_instructions_from_file()

    gui = ComputerGUI()

    keyboard_perf = KeyboardPeripheral()
    screen_perf = ScreenPeripheral()

    screen_perf.configure_gui(gui)
    keyboard_perf.configure_gui(gui)

    main_memory = MainMemory(1024, [keyboard_perf, screen_perf])
    program_memory = ProgramMemory(128)
    program_memory.load_program(instructions)

    cpu = Processor(main_memory, program_memory)

    gui.run(cpu.run)



