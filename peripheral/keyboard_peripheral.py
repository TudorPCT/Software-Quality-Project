from peripheral.peripherial import Peripheral, Int16, Int8
from tkinter import Frame
from gui.computer_gui import ComputerGUI
import tkinter as tk


keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '~', '|'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '#', '?', '@']
]


class KeyboardPeripheral(Peripheral):
    def __init__(self):
        super().__init__()
        self.keys = list[Int8]()
        self.main_frame: Frame = None

    @staticmethod
    def get_necessarily_memory_size() -> Int8:
        return Int8(1)

    def in_range(self, idx: Int16) -> bool:
        return self.assigned_memory_idx <= idx < self.assigned_memory_idx + Int16(self.get_necessarily_memory_size().
                                                                                  to_pyint())

    def print_report(self):
        print(f"Peripheral name: KeyboardPeripheral\nAssigned memory address: {self.assigned_memory_idx}\n"
              f"Memory size: {self.get_necessarily_memory_size()}\n{'=' * 20}\n")

    def __push_key(self, key_code: Int8):
        self.keys.append(key_code)

    def configure_gui(self, root: ComputerGUI) -> None:
        self.main_frame = Frame(root.window, bg='Powder Blue', width=1250, height=490)
        for line, keys_in_line in enumerate(keys):
            for col, key in enumerate(keys_in_line):
                tk.Button(self.main_frame, text=key, width=7, height=2,
                          command=lambda arg_key=key: self.__push_key(Int8(ord(arg_key)))).grid(row=line, column=col)

        self.main_frame.pack()

    def __getitem__(self, idx: Int8) -> Int8:
        assert (self.memory is not None) and (self.assigned_memory_idx is not None)
        if len(self.keys) == 0:
            return Int8(0)
        return self.keys.pop(0)

    def __setitem__(self, idx: Int8, val: Int8):
        raise NotImplementedError()
