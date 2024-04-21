from data_type.int8 import Int8
from data_type.int16 import Int16
from peripheral.peripherial import Peripheral


# 0 ->  n-s-p |    ->    n-s |       ->        n  |
# free_memory | stack memory | peripherals memory |

class MainMemory:
    def __init__(self, size: int, mapped_peripherals: list[Peripheral]):
        self.__memory: list[Int8] = [Int8(0) for _ in range(size)]

    def __getitem__(self, idx: Int16) -> Int16:
        assert idx.to_pyint() + 1 < len(self.__memory)
        address = idx.to_pyint()
        result = (self.__memory[address].to_pyint() << 8) | self.__memory[address + 1].to_pyint()
        return Int16(result)

    def __setitem__(self, idx: Int16, val: Int16):
        assert idx.to_pyint() + 1 < len(self.__memory)
        address = idx.to_pyint()

        rh = Int8(val.to_pyint())
        lh = Int8(val.to_pyint() >> 8)

        self.__memory[address] = lh
        self.__memory[address + 1] = rh

    def get_stack_base(self) -> Int16:
        return Int16(len(self.__memory))
