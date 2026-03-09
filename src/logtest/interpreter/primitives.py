from enum import Enum


class Primitive(Enum):
    false = "False"
    true = "True"

    def __str__(self) -> str:
        return self.value

