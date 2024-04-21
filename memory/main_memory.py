from data_type.int8 import Int8
from data_type.int16 import Int16
from peripheral.peripherial import Peripheral


# 0 ->  n-s-p |    ->    n-s |       ->        n  |
# free_memory | stack memory | peripherals memory |

class MainMemory:
    def __init__(self, size: int, mapped_peripherals: list[Peripheral]):
        self.__memory: list[Int8] = [Int8(0) for _ in range(size)]
        self.__mapped_peripherals, self.__reserved_memory_for_peripherals = \
            self.__peripherals_configure(mapped_peripherals)

        self.__print_peripherals_report()

    def __print_peripherals_report(self):
        for peripheral in self.__mapped_peripherals:
            peripheral.print_report()

    def __peripherals_configure(self, mapped_peripherals: list[Peripheral]) -> tuple[list[Peripheral], Int16]:
        reserved_memory_for_peripherals = Int16()

        for peripheral in mapped_peripherals:
            reserved_memory_for_peripherals += Int16(peripheral.get_necessarily_memory_size().to_pyint())
            peripheral.configure_memory(self, Int16(len(self.__memory) - 1) - reserved_memory_for_peripherals)

        return mapped_peripherals, reserved_memory_for_peripherals

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
        return Int16(len(self.__memory) - 2) - self.__reserved_memory_for_peripherals
