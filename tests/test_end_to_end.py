import unittest
import os

from src.gui.computer_gui import ComputerGUI
from src.peripheral.keyboard_peripheral import KeyboardPeripheral
from src.peripheral.screen_peripheral import ScreenPeripheral
from src.memory.main_memory import MainMemory
from src.memory.program_memory import ProgramMemory
from src.processor.processor import Processor, KillSwitch
from src.data_type.int16 import Int16
from src.processor.read_instructions import InstructionParser
from src.util.config_parser import get_data
from pathlib import Path


RES_DIR = os.path.join(str(Path(__file__).parent.absolute()), "resources")


def do_end_to_end_testing():
    instruction_parser = InstructionParser(
        os.path.join(RES_DIR, f"instructions_screen_keyboard.txt")
    )
    instructions = instruction_parser.read_instructions_from_file()

    config_data = get_data(os.path.join(RES_DIR, f"config{os.sep}config.txt"))

    gui = ComputerGUI()

    keyboard_perf = KeyboardPeripheral()
    screen_perf = ScreenPeripheral()

    screen_perf.configure_gui(gui)
    keyboard_perf.configure_gui(gui)

    main_memory = MainMemory(config_data["main_memory_size"], [keyboard_perf, screen_perf],
                             [Int16(config_data["keyboard_address"]), Int16(config_data["screen_address"])],
                             Int16(config_data["stack_address"]))

    program_memory = ProgramMemory(config_data["program_memory_size"])

    program_memory.load_program(instructions)

    cpu = Processor(main_memory, program_memory)

    kill_switch = KillSwitch()
    gui.run(lambda: cpu.run(kill_switch), lambda window: window.quit())
    kill_switch.kill = True

    print("Da")


DO_END_TO_END_TESTING = False


class TestStringMethods(unittest.TestCase):

    def test_gui(self):
        if DO_END_TO_END_TESTING:
            do_end_to_end_testing()

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
