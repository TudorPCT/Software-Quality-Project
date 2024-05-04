from gui.computer_gui import ComputerGUI
from peripheral.keyboard_peripheral import KeyboardPeripheral
from peripheral.screen_peripheral import ScreenPeripheral
from memory.main_memory import MainMemory
from memory.program_memory import ProgramMemory
from processor.processor import Processor
from data_type.int8 import Int8
from data_type.int16 import Int16
import time

from util.config_parser import get_data


def computer_run():
    print("da")
    time.sleep(5)
    screen_perf[Int8(10)] = Int8(35)
    time.sleep(1)
    screen_perf[Int8(20)] = Int8(35)
    time.sleep(1)
    screen_perf[Int8(30)] = Int8(35)
    time.sleep(1)
    screen_perf[Int8(40)] = Int8(35)
    time.sleep(1)
    screen_perf[Int8(50)] = Int8(35)


if __name__ == "__main__":
    config_data = get_data(r"D:\personal\Quality\Software-Quality-Project\resources\config\config_alabul.txt")

    gui = ComputerGUI()

    keyboard_perf = KeyboardPeripheral()
    screen_perf = ScreenPeripheral()

    screen_perf.configure_gui(gui)
    keyboard_perf.configure_gui(gui)

    main_memory = MainMemory(
        config_data["main_memory_size"],
        [keyboard_perf, screen_perf],
        [Int16(config_data["keyboard_address"]), Int16(config_data["screen_address"])],
        Int16(config_data["stack_address"])
    )
    program_memory = ProgramMemory(config_data["program_memory_size"])

    cpu = Processor(main_memory, program_memory)

    gui.run(computer_run)
