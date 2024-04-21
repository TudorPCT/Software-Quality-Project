from peripheral.peripherial import Peripheral, Int16, Int8
from gui.computer_gui import ComputerGUI
from tkinter import Frame
import tkinter as tk


class ScreenPeripheral(Peripheral):
    lines_nr = Int8(16)
    cols_nr = Int8(12)

    def __init__(self):
        super().__init__()
        self.pixels: list[list[tk.Label]] = [[None for _ in range(ScreenPeripheral.cols_nr.to_pyint())] 
                                             for _ in range(ScreenPeripheral.lines_nr.to_pyint())]
        self.main_frame: Frame = None


    @staticmethod
    def get_necessarily_memory_size() -> Int8:
        return ScreenPeripheral.lines_nr * ScreenPeripheral.cols_nr

    def print_report(self):
        print(f"Peripheral name: ScreenPeripheral\nAssigned memory address: {self.assigned_memory_idx}\n"
              f"Memory size: {self.get_necessarily_memory_size()}\n{'=' * 20}\n")

    def configure_gui(self, root: ComputerGUI) -> None:
        self.main_frame = Frame(root.window, bg='black', width=1250, height=490)
        for i in range(ScreenPeripheral.lines_nr.to_pyint()):
            for j in range(ScreenPeripheral.cols_nr.to_pyint()):
                 frame = tk.Frame(
                   master=self.main_frame,
                   relief=tk.FLAT,
                   borderwidth=1
                 )
                 frame.grid(row=i, column=j)
                 self.pixels[i][j] = tk.Label(master=frame, bg="black", fg="white", height=2, width=4, padx=0, pady=0)
                 self.pixels[i][j].pack()

        self.main_frame.pack()
         

    def __getitem__(self, idx: Int8) -> Int8:
        raise NotImplementedError()

    def __setitem__(self, idx: Int8, val: Int8):
        assert (self.memory is not None) and (self.assigned_memory_idx is not None)
        line_idx = idx.to_pyint() // ScreenPeripheral.cols_nr.to_pyint()
        col_idx = idx.to_pyint() % ScreenPeripheral.cols_nr.to_pyint()

        assert line_idx < ScreenPeripheral.lines_nr.to_pyint()
        assert col_idx < ScreenPeripheral.cols_nr.to_pyint()

        self.pixels[line_idx][col_idx].config(text=chr(val.to_pyint()))
        
