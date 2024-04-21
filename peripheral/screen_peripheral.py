from peripheral.peripherial import Peripheral, Int16, Int8, MainMemory
from gui.computer_gui import ComputerGUI


class ScreenPeripheral(Peripheral):
    def __init__(self):
        super().__init__()
        self.keys = list[Int8]()

    def configure_gui(self, root: ComputerGUI) -> None:
        raise NotImplementedError()

    def __getitem__(self, idx: Int8) -> Int8:
        raise NotImplementedError()

    def __setitem__(self, idx: Int8, val: Int8):
        assert (self.__memory is not None) and (self.__assigned_memory_idx is not None)

