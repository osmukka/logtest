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
        self._input = Peekable([])
        self._output = []

        self._operator_lengths = list({len(key) for key in operators}).sorted(reverse=True)


    def _tokenize_operator(self) -> None:
        for length in self._operator_lengths:
            op = self._input.peek(length)
            if op in operators:
                self._output.append(Token(op))
                return
        



