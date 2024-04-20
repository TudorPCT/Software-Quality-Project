class Flag:
    def __init__(self, value=False):
        self.value = value

    def to_pybool(self) -> bool:
        return self.value

    def __or__(self, other: "Flag") -> "Flag":
        return Flag(self.value or other.value)