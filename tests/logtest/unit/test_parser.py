import pytest

from logtest.parser.parser import Parser
from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode, AST_UnaryNode, AST_BinaryNode
from logtest.tokenizer.tokenizer import Tokenizer
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


def parse(tokens: list[Token]) -> AST_Node:
    return Parser().parse(tokens)

class TestParser:
    def test_parse_identifiers(self):
        ast = parse([
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.EOF)
              ])

        assert ast == AST_TerminalNode("True")


    def test_parse_not(self):
        ast = parse([
                  Token(TokenKind.Not),
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.EOF)
              ])

        assert ast == AST_UnaryNode(
                          TokenKind.Not,
                          AST_TerminalNode("True")
                      )


    def test_parse_or(self):
        ast = parse([
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.Or),
                  Token(TokenKind.Identifier, "False"),
                  Token(TokenKind.EOF)
              ])

        assert ast == AST_BinaryNode(
                          AST_TerminalNode("True"),
                          TokenKind.Or,
                          AST_TerminalNode("False")
                      )


    def test_parse_and(self):
        ast = parse([
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.And),
                  Token(TokenKind.Identifier, "False"),
                  Token(TokenKind.EOF)
              ])

        assert ast == AST_BinaryNode(
                          AST_TerminalNode("True"),
                          TokenKind.And,
                          AST_TerminalNode("False")
                      )


    def test_parse_impl(self):
        ast = parse([
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.Impl),
                  Token(TokenKind.Identifier, "False"),
                  Token(TokenKind.EOF)
              ])

        assert ast == AST_BinaryNode(
                          AST_TerminalNode("True"),
                          TokenKind.Impl,
                          AST_TerminalNode("False")
                      )


    def test_parse_iff(self):
        ast = parse([
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.Iff),
                  Token(TokenKind.Identifier, "False"),
                  Token(TokenKind.EOF)
              ])

        assert ast == AST_BinaryNode(
                          AST_TerminalNode("True"),
                          TokenKind.Iff,
                          AST_TerminalNode("False")
                      )


    def test_parse_parentheses(self):
        ast = parse([
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.And),
                  Token(TokenKind.LParen),
                  Token(TokenKind.Identifier, "False"),
                  Token(TokenKind.And),
                  Token(TokenKind.Identifier, "True"),
                  Token(TokenKind.RParen),
                  Token(TokenKind.EOF)
              ])

        assert ast == AST_BinaryNode(
                          AST_TerminalNode("True"),
                          TokenKind.And,
                          AST_BinaryNode(
                              AST_TerminalNode("False"),
                              TokenKind.And,
                              AST_TerminalNode("True")
                          )
                      )


    def test_parse_missing_right_parenthesis(self):
        with pytest.raises(ValueError):
            parse([
                Token(TokenKind.LParen),
                Token(TokenKind.EOF)
            ])


    def test_parse_wrong_left_hand_side(self):
        with pytest.raises(ValueError):
            parse([
                Token(TokenKind.And),
                Token(TokenKind.And),
                Token(TokenKind.EOF)
            ])

