import tkinter as tk
from typing import Optional
from typing import Callable
from threading import Thread
import time


class ComputerGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.__computer_thread: Thread = None
        self.__killer_thread: Thread = None

    def run(self, computer_thread_fn: Callable, kill_callback: Optional[Callable] = None):
        self.__computer_thread = Thread(target=self.__computer_runner, args=[computer_thread_fn])
        self.__computer_thread.start()

        if kill_callback is not None:
            self.__killer_thread = Thread(target=self.__kill_runner, args=[kill_callback])
            self.__killer_thread.start()

        self.window.mainloop()

    def __computer_runner(self, fn: Callable):
        time.sleep(1)  # bootup
        fn()

    def __kill_runner(self, fn: Callable):
        time.sleep(5)
        fn(self.window)
