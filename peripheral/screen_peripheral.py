from peripheral.peripherial import Peripheral, Int16, Int8
from gui.computer_gui import ComputerGUI


class ScreenPeripheral(Peripheral):
    lines_nr = Int8(16)
    cols_nr = Int8(12)

    def __init__(self):
        super().__init__()
        self.keys = list[Int8]()

    @staticmethod
    def get_necessarily_memory_size() -> Int8:
        return ScreenPeripheral.lines_nr * ScreenPeripheral.cols_nr

    def print_report(self):
        print(f"Peripheral name: ScreenPeripheral\nAssigned memory address: {self.assigned_memory_idx}\n"
              f"Memory size: {self.get_necessarily_memory_size()}\n{'=' * 20}\n")

    def configure_gui(self, root: ComputerGUI) -> None:
        raise NotImplementedError()

    def __getitem__(self, idx: Int8) -> Int8:
        raise NotImplementedError()

    def __setitem__(self, idx: Int8, val: Int8):
        assert (self.__memory is not None) and (self.__assigned_memory_idx is not None)

