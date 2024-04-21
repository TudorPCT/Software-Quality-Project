from gui.computer_gui import ComputerGUI
from peripheral.keyboard_peripheral import KeyboardPeripheral
from peripheral.screen_peripheral import ScreenPeripheral
from memory.main_memory import MainMemory
from memory.program_memory import ProgramMemory
from processor.processor import Processor
from data_type.int8 import Int8
import time
from threading import Thread


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
    gui = ComputerGUI()

    keyboard_perf = KeyboardPeripheral()
    screen_perf = ScreenPeripheral()

    screen_perf.configure_gui(gui)
    keyboard_perf.configure_gui(gui)

    main_memory = MainMemory(1024, [keyboard_perf, screen_perf])
    program_memory = ProgramMemory(128)

    cpu = Processor(main_memory, program_memory)

    gui.run(computer_run)



