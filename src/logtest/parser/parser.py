from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode, AST_UnaryNode, AST_BinaryNode
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


unary_binding_powers = {
    TokenKind.Not: (0, 9),
    TokenKind.LParen: (0, 0),
    TokenKind.RParen: (0, 0),
}

binary_binding_powers = {
    TokenKind.Or: (1, 2),
    TokenKind.And: (3, 4),
    TokenKind.Impl: (6, 5),
    TokenKind.Iff: (7, 8)
}


class Parser:
    def __init__(self) -> None:
        self._tokens = []
        self._i = 0


    def _tokens_left(self) -> int:
        return len(self._tokens) - self._i


    def _peek(self) -> Token | None:
        if not self._tokens_left():
            return None

        return self._tokens[self._i]


    def _consume(self) -> Token | None:
        token = self._peek()
        if token:
            self._i += 1
        return token


    def _reverse(self) -> None:
        if self._i > 0:
            self._i -= 1


    def _expect(self, kind: TokenKind) -> None:
        if self._peek() and self._peek().kind is kind:
            self._consume()
        else:
            raise ValueError(f"Unexpected token while parsing: {self._peek()} at index {self._i}")


    def _nud(self) -> AST_Node | None:
        token = self._consume()
        match token.kind:
            case TokenKind.Boolean:
                return AST_TerminalNode(token.value)
            case TokenKind.Not:
                operand = self._parse_expression()
                return AST_UnaryNode(token.kind, operand)
            case TokenKind.LParen:
                expression = self._parse_expression()
                self._expect(TokenKind.RParen)
                return expression
            case TokenKind.RParen:
                self._reverse()


    def parse(self, tokens: list[Token]) -> AST_Node:
        self._tokens = tokens
        self._i = 0
        return self._parse_expression()


    def _parse_expression(self) -> AST_Node:
        return self._parse_binary_expression()


    def _parse_binary_expression(self, min_bp: int=0) -> AST_Node:
        lhs = self._nud()

        while True:
            operator = self._peek()
            if not operator or operator.kind not in binary_binding_powers:
                break
            lbp, rbp = binary_binding_powers[operator.kind]
            if lbp < min_bp:
                break
            self._consume()
            rhs = self._parse_binary_expression(rbp)
            lhs = AST_BinaryNode(lhs, operator.kind, rhs)
        return lhs

