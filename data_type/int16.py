class Int16:
    def __init__(self, value=0):
        if value < 0:
            value = 0
        value = value & 65535
        self._value = value

    def __repr__(self):
        return f"Int16({self._value})"

    def __str__(self):
        return str(self._value)

    def __add__(self, other):
        return Int16(self._value + other._value)

    def __sub__(self, other):
        return Int16(self._value - other._value)

    def __mul__(self, other):
        return Int16(self._value * other._value)

    def __truediv__(self, other):
        return Int16(self._value // other._value)

    def __mod__(self, other):
        return Int16(self._value % other._value)

    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self._value < other._value

    def __gt__(self, other):
        return self._value > other._value

    def __le__(self, other):
        return self._value <= other._value

    def __ge__(self, other):
        return self._value >= other._value

    def __and__(self, other):
        return Int16(self._value & other._value)

    def __or__(self, other):
        return Int16(self._value | other._value)

    def __xor__(self, other):
        return Int16(self._value ^ other._value)

    def __invert__(self):
        return Int16(~self._value)

    def __lshift__(self, shift):
        return Int16(self._value << shift)

    def __rshift__(self, shift):
        return Int16(self._value >> shift)

    def to_bits(self):
        return bin(self._value)[2:].zfill(16)

    def to_pyint(self) -> int:
        return self._value


if __name__ == '__main__':
    a = Int16(0b1111111111111111)  # Maximum 16-bit value
    b = Int16(0b0000000000000001)  # Minimum 16-bit value

    print("a =", a)  # Output: a = 65535
    print("b =", b)  # Output: b = 1

    c = a + b
    print("c =", c)  # Output: c = 0 (Wraps around due to overflow)

    d = a & Int16(0b1111000011110000)  # Bitwise AND
    print("d =", d)  # Output: d = 61440

    e = ~b  # Bitwise NOT
    print("e =", e)  # Output: e = -2 (due to two's complement representation)

    a = Int16(65536)  # Providing a value larger than 16-bit range
    print("a =", a)  # Output: a = 65535 (maximum allowed value)

    b = Int16(100)  # Providing a value within the 16-bit range
    print("b =", b)  # Output: b = 100
