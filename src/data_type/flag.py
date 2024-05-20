class Flag:
    def __init__(self, value=False):
        self.value = value

    def to_pybool(self) -> bool:
        return self.value

    def __or__(self, other: "Flag") -> "Flag":
        return Flag(self.value or other.value)

    def __hash__(self):
        return hash(self.value)

    def __not__(self) -> "Flag":
        return Flag(not self.value)
