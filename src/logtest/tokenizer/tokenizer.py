from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


max_len = 3
operators = {
    "-": TokenKind.Not,
    "&&": TokenKind.And,
    "||": TokenKind.Or,
    "->": TokenKind.Impl,
    "<->": TokenKind.Iff,
    "=": TokenKind.Assign,
    "(": TokenKind.LParen,
    ")": TokenKind.RParen
}


class Tokenizer:
    def __init__(self) -> None:
        self._input = ""
        self._output = []
        self._i = 0


    def _items_left(self) -> int:
        return len(self._input) - self._i


    def _peek(self, count=1) -> str | None:
        if count < 1:
            raise ValueError("Cannot peek under 1 item")

        if count > self._items_left():
            return None
        if self._i < len(self._input):
            return self._input[self._i : self._i+count]
        else:
            return None


    def _consume(self, count=1) -> str | None:
        slice = self._peek(count)
        if slice:
            self._i += count
        return slice


    def _tokenize_identifier(self) -> None:
        identifier = ""
        while self._peek() and self._peek().isalpha():
            identifier += self._consume()
        
        token = Token(TokenKind.Identifier, identifier)
        self._output.append(token)


    def _tokenize_operator(self) -> None:
        for length in range(max_len, 0, -1):
            op = self._peek(length)
            if op in operators:
                self._consume(length)
                self._output.append(Token(operators[op]))
                return

        self._output.append(Token(TokenKind.Error, (op, self._i)))
        self._consume(length)
            
    def tokenize(self, chars: str) -> list[Token]:
        self._input = chars
        self._output = []
        self._i = 0

        while self._items_left():
            if self._peek() in " \t\n":
                self._consume()
                continue
            if self._peek().isalpha():
                self._tokenize_identifier()
            else:
                self._tokenize_operator()
        self._output.append(Token(TokenKind.EOF))
        return self._output

