import pytest

from logtest.tokenizer.tokenizer import Tokenizer
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


def tokenize(string: str) -> list[Token]:
    return Tokenizer().tokenize(string)


class TestTokenize:
    def test_tokenizing_operators(self):
        assert tokenize("-")[0] == Token(TokenKind.Not)
        assert tokenize("&&")[0] == Token(TokenKind.And)
        assert tokenize("||")[0] == Token(TokenKind.Or)
        assert tokenize("->")[0] == Token(TokenKind.Impl)
        assert tokenize("<->")[0] == Token(TokenKind.Iff)
        assert tokenize("=")[0] == Token(TokenKind.Assign)
        assert tokenize("(")[0] == Token(TokenKind.LParen)
        assert tokenize(")")[0] == Token(TokenKind.RParen)
        assert tokenize("<")[0] == Token(TokenKind.Error, ("<", 0))

    def test_tokenizing_identifiers(self):
        assert tokenize("True")[0] == Token(TokenKind.Identifier, "True")
        assert tokenize("False")[0] == Token(TokenKind.Identifier, "False")
        assert tokenize("test")[0] == Token(TokenKind.Identifier, "test")

    def test_tokenizing_empty_string(self):
        assert tokenize("") == [Token(TokenKind.EOF)]

    def test_tokenizer_errors(self):
        assert tokenize("1")[0] == Token(TokenKind.Error, ("1", 0))


