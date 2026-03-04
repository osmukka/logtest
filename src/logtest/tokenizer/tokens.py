from dataclasses import dataclass

from logtest.tokenizer.token_kinds import TokenKind

@dataclass
class Token:
    kind: TokenKind
    value: bool | None = None

    def __str__(self) -> str:
        value = self.value if self.value else ''
        return f"Token({self.kind}{value})"

