import tkinter as tk
from typing import Optional
from typing import Callable
from threading import Thread
import time


class ComputerGUI:
    def __init__(self):
        self.window = tk.Tk()

    def run(self, computer_thread_fn: Callable, kill_callback: Optional[Callable] = None):
        Thread(target=self.computer_runner, args=[computer_thread_fn]).start()

        if kill_callback is not None:
            Thread(target=self.kill_tunner, args=[kill_callback]).start()

        self.window.mainloop()

    def computer_runner(self, fn: Callable):
        time.sleep(1)  # bootup
        fn()

    def kill_tunner(self, fn: Callable):
        time.sleep(5)
        fn(self.window)
