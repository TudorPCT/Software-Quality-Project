from gui.computer_gui import ComputerGUI
from peripheral.keyboard_peripheral import KeyboardPeripheral
from peripheral.screen_peripheral import ScreenPeripheral
from memory.main_memory import MainMemory
from memory.program_memory import ProgramMemory
from processor.processor import Processor


if __name__ == "__main__":
    gui = ComputerGUI()

    keyboard_perf = KeyboardPeripheral()
    keyboard_perf.configure_gui(gui)

    screen_perf = ScreenPeripheral()
    #screen_perf.configure_gui(gui)

    main_memory = MainMemory(1024, [keyboard_perf, screen_perf])
    program_memory = ProgramMemory(128)

    cpu = Processor(main_memory, program_memory)

    gui.run()
