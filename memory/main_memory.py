import numpy as np
from data_type.int16 import Int16


class MainMemory:
    def __init__(self, size: int):
        self.__memory = np.zeros(size, dtype=np.int16)

    def __getitem__(self, idx: Int16) -> Int16:
        return Int16(self.__memory[idx.to_pyint()])

    def __setitem__(self, idx: Int16, val: Int16):
        self.__memory[idx.to_pyint()] = val.to_pyint()
