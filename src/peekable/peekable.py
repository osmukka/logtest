from typing import Any


class Peekable:
    def __init__(self, cont: list) -> None:
        if type(cont) != list:
            raise TypeError("Peekable must take a list.")
        self._contents = cont.copy()
        self._i = 0


    def items_left(self) -> int:
        return len(self._contents) - self._i


    def peek(self, count: int=1) -> Any | None:
        if count > self.items_left():
            return None
        elif count <= self.items_left() and count > 1:
            return self._contents[self._i:self._i+count]
        elif count == 1:
            return self._contents[self._i]
        else:
            raise ValueError(f"Can't peek under 1 items.")


    def advance(self, count: int=1) -> Any | None:
        value = self.peek(count)
        if value:
            self._i += count
        return value
