import pytest

from logtest.tokenizer.tokenizer import Tokenizer
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


@pytest.fixture
def tokenizer():
    return Tokenizer()


class TestTokenize:
    def test_tokenize_operators(self, tokenizer):
        assert tokenizer.tokenize("-")[0] == Token(TokenKind.Not)
        assert tokenizer.tokenize("&&")[0] == Token(TokenKind.And)
        assert tokenizer.tokenize("||")[0] == Token(TokenKind.Or)
        assert tokenizer.tokenize("->")[0] == Token(TokenKind.Impl)
        assert tokenizer.tokenize("<->")[0] == Token(TokenKind.Iff)
        assert tokenizer.tokenize("=")[0] == Token(TokenKind.Assign)
        assert tokenizer.tokenize("(")[0] == Token(TokenKind.LParen)
        assert tokenizer.tokenize(")")[0] == Token(TokenKind.RParen)
        assert tokenizer.tokenize("<")[0] == Token(TokenKind.Error, ("<", 0))


    def test_tokenize_identifiers(self, tokenizer):
        assert tokenizer.tokenize("True")[0] == Token(TokenKind.Boolean, True)
        assert tokenizer.tokenize("False")[0] == Token(TokenKind.Boolean, False)
        assert tokenizer.tokenize("test")[0] == Token(TokenKind.Prep, "test")

