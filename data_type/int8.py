class Int8:
    def __init__(self, value=0):
        if value < 0:
            value = 0
        elif value > 255:
            value = 255
        self._value = value

    def __repr__(self):
        return f"Int8({self._value})"

    def __str__(self):
        return str(self._value)

    def __add__(self, other):
        return Int8(self._value + other._value)

    def __sub__(self, other):
        return Int8(self._value - other._value)

    def __mul__(self, other):
        return Int8(self._value * other._value)

    def __truediv__(self, other):
        return Int8(self._value // other._value)

    def __mod__(self, other):
        return Int8(self._value % other._value)

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
        return Int8(self._value & other._value)

    def __or__(self, other):
        return Int8(self._value | other._value)

    def __xor__(self, other):
        return Int8(self._value ^ other._value)

    def __invert__(self):
        return Int8(~self._value)

    def __lshift__(self, shift):
        return Int8(self._value << shift)

    def __rshift__(self, shift):
        return Int8(self._value >> shift)

    def to_bits(self):
        return bin(self._value)[2:].zfill(16)


if __name__ == '__main__':
    a = Int8(256)  # Providing a value larger than 8-bit range
    print("a =", a)  # Output: a = 255 (maximum allowed value)

    b = Int8(100)  # Providing a value within the 8-bit range
    print("b =", b)  # Output: b = 100

    c = Int8(0b1111111111)  # Providing a value larger than 8-bit range
    print("c =", c) # Output: c = 255 (maximum allowed value)
