from gui.computer_gui import ComputerGUI
from peripheral.keyboard_peripheral import KeyboardPeripheral


if __name__ == "__main__":
    gui = ComputerGUI()
    keyboard_perf = KeyboardPeripheral()
    keyboard_perf.configure_gui(gui)

    gui.run()
