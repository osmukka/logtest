from peekable.peekable import Peekable
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


max_len = 3
operators = {
    "-": TokenKind.Not,
    "&&": TokenKind.And,
    "||": TokenKind.Or,
    "->": TokenKind.Impl,
    "<->": TokenKind.Iff,
    "=": TokenKind.Assign
}


class Tokenizer:
    def __init__(self) -> None:
        self._input = ""
        self._output = []
        self._i = 0


    def _peek(self, count=1) -> str | None:
        if count < 1:
            raise ValueError("Cannot peek under 1 item")

        if self._i < len(self._input):
            return self._input[self._i : self._i+count]
        else:
            return None


    def _consume(self, count=1) -> str | None:
        slice = self._peek(count)
        if slice:
            self._i += count
        return slice


    def _tokenizer_identifier(self) -> None:
        identifier_length = 1
        while self._peek(identifier_length).isalpha():
            identifier_length += 1
        identifier_length -= 1

        identifier_string = self._consume(identifier_length)
        self._output.append(Token(TokenKind.Prep, identifier_string))



    def _tokenize_operator(self) -> None:
        for length in range(max_len, 0, -1):
            op = self._peek(length)
            if op in operators:
                self._consume(length)
                self._output.append(Token(operators[op]))
                break
            
    def tokenize(self, chars: str) -> list[Token]:
        self._input = chars
        self._output = []
        self._i = 0

        while self._peek():
            if self._peek().isalpha():
                self._tokenize_identifier()
            else:
                self._tokenize_operator()
        return self._output
            
        



