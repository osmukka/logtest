from peekable.peekable import Peekable
from tokenizer.tokens import Token
from tokenizer.token_kinds import TokenKind


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
        self._input = Peekable([])
        self._output = []

        self._operator_lengths = list({len(key) for key in operators}).sorted(reverse=True)


    def _tokenizer_identifier(self) -> None:
        identifier_length = 1
        while self._input.peek(identifier_length).isalpha():
            identifier_length += 1
        identifier_length -= 1

        identifier_string = self._input.consume(identifier_length)
        self._output.append(Token(TokenKind.Prep, identifier_string))



    def _tokenize_operator(self) -> None:
        for length in self._operator_lengths:
            op = self._input.peek(length)
            if op in operators:
                self._input.consume(length)
                self._output.append(Token(op))
            
    def tokenize(self, chars: list[str]) -> list[Token]:
        self._input = Peekable(chars)
        self._output = []

        while self._input.peek():
            if self._input.peek().isalpha():
                self._tokenize_identifier()
            else:
                self._tokenize_operator()
        return self._output()
            
        



