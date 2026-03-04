import pytest

from logtest.tokenizer.tokenizer import Tokenizer
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


@pytest.fixture
def tokenizer():
    return Tokenizer()


class TestTokenize:
    def test_tokenize_operators(self, tokenizer):
        assert tokenizer.tokenize("-") == [Token(TokenKind.Not)]
        assert tokenizer.tokenize("&&") == [Token(TokenKind.And)]
        assert tokenizer.tokenize("||") == [Token(TokenKind.Or)]
        assert tokenizer.tokenize("->") == [Token(TokenKind.Impl)]
        assert tokenizer.tokenize("<->") == [Token(TokenKind.Iff)]
        assert tokenizer.tokenize("=") == [Token(TokenKind.Assign)]
        assert tokenizer.tokenize("(") == [Token(TokenKind.LParen)]
        assert tokenizer.tokenize(")") == [Token(TokenKind.RParen)]


    def test_tokenize_identifiers(self, tokenizer):
        assert tokenizer.tokenize("True") == [Token(TokenKind.Boolean, True)]
        assert tokenizer.tokenize("False") == [Token(TokenKind.Boolean, False)]
        assert tokenizer.tokenize("test") == [Token(TokenKind.Prep, "test")]

