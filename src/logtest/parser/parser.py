from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode, AST_BinaryNode
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


binding_powers = {
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
        t = self._peek()
        if t:
            self._i += 1
        return t


    def _nud(self) -> AST_Node:
        t = self._consume()
        match t.kind:
            case TokenKind.TruthVal:
                return AST_TerminalNode(t.value)


    def parse(self, tokens: list[Token]) -> AST_Node:
        self._tokens = tokens
        self._i = 0
        return self._parse_binary_expression()


    def _parse_binary_expression(self, min_bp: int=0) -> AST_Node:
        lhs = self._nud()

        while True:
            operator = self._peek()
            if not operator or operator.kind not in binding_powers:
                break
            lbp, rbp = binding_powers[operator.kind]
            if lbp < min_bp:
                break
            self._consume()
            rhs = self._parse_binary_expression(rbp)
            lhs = AST_BinaryNode(lhs, operator.kind, rhs)
        return lhs

