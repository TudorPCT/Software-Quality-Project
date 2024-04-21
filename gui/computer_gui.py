import tkinter as tk
from typing import Callable
from threading import Thread
import time


class ComputerGUI:
    def __init__(self):
        self.window = tk.Tk()

    def run(self, computer_thread_fn: Callable):
        Thread(target=self.computer_runner, args=[computer_thread_fn]).start()
        self.window.mainloop()

    def computer_runner(self, fn: Callable):
        time.sleep(1) # bootup
        fn()