from peekable.peekable import Peekable
from tokens import Token
from token_kinds import TokenKind


operators = {
    "-": TokenKind.Not,
    "&&": TokenKind.And,
    "AND": TokenKind.And,
    "||": TokenKind.Or,
    "OR": TokenKind.Or,
    "->": TokenKind.Impl,
    "IMPLIES": TokenKind.Impl,
    "<->": TokenKind.Iff,
    "IFF": TokenKind.Iff,
    "=": TokenKind.Assign
}


class Tokenizer:
    def __init__(self) -> None:
        self.input = Peekable([])
        self.output = []


    def tokenize_operator(self) -> None:



