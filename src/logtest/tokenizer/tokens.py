from dataclasses import dataclass

@dataclass
class Token:
    kind: TokenKind
    value: str | bool | None = None

    def __str__(self) -> str:
        value = self.value if self.value else ''
        return f"Token({self.kind}{value})"

