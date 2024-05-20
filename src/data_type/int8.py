class Int8:
    def __init__(self, value=0):
        if value < 0:
            value = 0
        value = value & 255
        self._value = value

    def __repr__(self):
        return f"Int8({self._value})"

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self._value)

    def __add__(self, other):
        return Int8(self._value + other.value)

    def __sub__(self, other):
        return Int8(self._value - other.value)

    def __mul__(self, other):
        return Int8(self._value * other.value)

    def __truediv__(self, other):
        return Int8(self._value // other.value)

    def __mod__(self, other):
        return Int8(self._value % other.value)

    def __eq__(self, other):
        return self._value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self._value < other.value

    def __gt__(self, other):
        return self._value > other.value

    def __le__(self, other):
        return self._value <= other.value

    def __ge__(self, other):
        return self._value >= other.value

    def __and__(self, other):
        return Int8(self._value & other.value)

    def __or__(self, other):
        return Int8(self._value | other.value)

    def __xor__(self, other):
        return Int8(self._value ^ other.value)

    def __invert__(self):
        return Int8(~self._value)

    def __lshift__(self, shift):
        return Int8(self._value << shift)

    def __rshift__(self, shift):
        return Int8(self._value >> shift)

    def __hash__(self):
        return hash(self.value)

    def to_bits(self):
        return bin(self._value)[2:].zfill(16)

    def to_pyint(self) -> int:
        return self._value
