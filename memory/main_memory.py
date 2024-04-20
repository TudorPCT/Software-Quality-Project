import numpy as np
from data_type.int16 import Int16


class MainMemory:
    def __init__(self, size: int):
        self.__memory = np.array(size, dtype=np.int16)

    def __getitem__(self, idx) -> Int16:
        return Int16(self.__memory[idx])

    def __setitem__(self, idx, val: Int16):
        self.__memory[idx] = val.to_pyint()
