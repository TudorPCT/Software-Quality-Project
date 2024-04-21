from data_type.int16 import Int16
from data_type.int8 import Int8
from typing import TYPE_CHECKING
from tkinter import Label, Frame
from gui.computer_gui import ComputerGUI
if TYPE_CHECKING:
    from memory.main_memory import MainMemory


class Peripheral:
    def __init__(self):
        self.__memory: 'MainMemory' = None
        self.__assigned_memory_idx: Int16 = None

    @property
    def memory(self) -> 'MainMemory':
        return self.__memory

    @property
    def assigned_memory_idx(self) -> Int16():
        return self.__assigned_memory_idx

    @staticmethod
    def get_necessarily_memory_size() -> Int8:
        raise NotImplementedError()

    def print_report(self):
        raise NotImplementedError()

    def configure_memory(self, memory: 'MainMemory', assigned_memory_idx: Int16) -> None:
        self.__memory = memory
        self.__assigned_memory_idx = assigned_memory_idx

    def configure_gui(self, root: ComputerGUI) -> None:
        raise NotImplementedError()

    def __getitem__(self, idx: Int8) -> Int8:
        raise NotImplementedError()

    def __setitem__(self, idx: Int8, val: Int8):
        raise NotImplementedError()
