from typing import Any


class Peekable:
    def __init__(self, cont: list) -> None:
        self._contents = cont.copy()
        self._i = 0

    def items_left(self) -> int:
        return len(self._contents) - self._i

    def peek(self, count: int=1) -> Any | None:
        if length <= self.items_left():
            return self._contents[self._i:self._i+count]
        return None

    def advance(self, count: int=1) -> Any | None:
        value = self.peek(count)
        if value:
            self._i += count
        return value
