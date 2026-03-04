import pytest

from logtest.parser.parser import Parser
from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode, AST_BinaryNode
from logtest.tokenizer.tokenizer import Tokenizer
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


def parse(string: str) -> AST_Node:
    tokens = Tokenizer().tokenize(string)
    return Parser().parse(tokens)

class TestParser:
    def test_parse_booleans(self):
        assert parse("True") == AST_TerminalNode(True)
        assert parse("False") == AST_TerminalNode(False)


    def test_parse_not(self):
        ast = parse("-True")
        assert ast.op is TokenKind.Not
        assert ast.operand == AST_TerminalNode(True)


    def test_parse_or(self):
        ast = parse("True || False")
        assert ast.op is TokenKind.Or
        assert ast.left == AST_TerminalNode(True)
        assert ast.right == AST_TerminalNode(False)


    def test_parse_and(self):
        ast = parse("True && False")
        assert ast.op is TokenKind.And
        assert ast.left == AST_TerminalNode(True)
        assert ast.right == AST_TerminalNode(False)


    def test_parse_impl(self):
        ast = parse("True -> False")
        assert ast.op is TokenKind.Impl
        assert ast.left == AST_TerminalNode(True)
        assert ast.right == AST_TerminalNode(False)


    def test_parse_iff(self):
        ast = parse("True <-> False")
        assert ast.op is TokenKind.Iff
        assert ast.left == AST_TerminalNode(True)
        assert ast.right == AST_TerminalNode(False)
        

    def test_parse_parentheses(self):
        ast = parse("True<->(False<->True)")
        assert ast.op is TokenKind.Iff
        assert ast.right.op is TokenKind.Iff
        assert ast.right.left == AST_TerminalNode(False)
        assert ast.right.right == AST_TerminalNode(True)

