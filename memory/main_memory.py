from data_type.int8 import Int8
from data_type.int16 import Int16
from peripheral.peripherial import Peripheral
from typing import Optional


# 0 ->  n-s-p |    ->    n-s |       ->        n  |
# free_memory | stack memory | peripherals memory |

class MainMemory:
    def __init__(self, size: int, mapped_peripherals: list[Peripheral],
                 assigned_peripherals_addresses: Optional[list[Int16]] = None,
                 stack_address: Optional[Int16] = None):

        assert size % 1024 == 0
        assert size < 65536

        self.__memory: list[Int8] = [Int8(0) for _ in range(size)]

        assert (assigned_peripherals_addresses is None) == (stack_address is None)

        if assigned_peripherals_addresses is None:
            self.__mapped_peripherals, self.__stack_address = self.__peripherals_configure(mapped_peripherals)
        else:
            self.__mapped_peripherals = self.__peripherals_configure_from_received(
                mapped_peripherals,
                assigned_peripherals_addresses
            )
            self.__stack_address = stack_address

        self.__print_peripherals_report()

    def __print_peripherals_report(self):
        for peripheral in self.__mapped_peripherals:
            peripheral.print_report()

    def __peripherals_configure(self, mapped_peripherals: list[Peripheral]) -> tuple[list[Peripheral], Int16]:
        reserved_memory_for_peripherals = Int16()

        for peripheral in mapped_peripherals:
            reserved_memory_for_peripherals += Int16(peripheral.get_necessarily_memory_size().to_pyint())
            peripheral.configure_memory(self, Int16(len(self.__memory) - 1) - reserved_memory_for_peripherals)

        return mapped_peripherals, Int16(len(self.__memory) - 3) - reserved_memory_for_peripherals

    def __peripherals_configure_from_received(self, mapped_peripherals: list[Peripheral],
                                              assigned_peripherals_addresses: Optional[list[Int16]]) -> list[Peripheral]:

        for peripheral, assigned_addresses in zip(mapped_peripherals, assigned_peripherals_addresses):
            peripheral.configure_memory(self, assigned_addresses)

        return mapped_peripherals

    def __getitem__(self, idx: Int16) -> Int16:
        assert idx.to_pyint() + 1 < len(self.__memory)

        for peripheral in self.__mapped_peripherals:
            if peripheral.in_range(idx):
                return Int16(peripheral[idx - peripheral.assigned_memory_idx].to_pyint())

        address = idx.to_pyint()
        result = (self.__memory[address].to_pyint() << 8) | self.__memory[address + 1].to_pyint()
        return Int16(result)

    def __setitem__(self, idx: Int16, val: Int16):
        assert idx.to_pyint() + 1 < len(self.__memory)

        address = idx.to_pyint()

        for peripheral in self.__mapped_peripherals:
            if peripheral.in_range(idx):
                self.__memory[address] = Int8(val.to_pyint())
                peripheral[idx - peripheral.assigned_memory_idx] = self.__memory[address]
                return

        rh = Int8(val.to_pyint())
        lh = Int8(val.to_pyint() >> 8)

        self.__memory[address] = lh
        self.__memory[address + 1] = rh

    def get_stack_base(self) -> Int16:
        return self.__stack_address
