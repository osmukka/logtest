import pytest

from logtest.tokenizer.tokenizer import Tokenizer
from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


@pytest.fixture
def new_tokenizer():
    return Tokenizer()


class TestTokenize:
    def test_tokenize_individual_operators(self, new_tokenizer):
        assert new_tokenizer.tokenize("-") == [Token(TokenKind.Not)]
        assert new_tokenizer.tokenize("&&") == [Token(TokenKind.And)]
        assert new_tokenizer.tokenize("||") == [Token(TokenKind.Or)]
        assert new_tokenizer.tokenize("->") == [Token(TokenKind.Impl)]
        assert new_tokenizer.tokenize("<->") == [Token(TokenKind.Iff)]
        assert new_tokenizer.tokenize("=") == [Token(TokenKind.Assign)]

    def test_tokenize_all_operators(self, new_tokenizer):
        operator_tokens = new_tokenizer.tokenize("-&&||-><->=")
        assert operator_tokens[0] == Token(TokenKind.Not)
        assert operator_tokens[1] == Token(TokenKind.And)
        assert operator_tokens[2] == Token(TokenKind.Or)
        assert operator_tokens[3] == Token(TokenKind.Impl)
        assert operator_tokens[4] == Token(TokenKind.Iff)
        assert operator_tokens[5] == Token(TokenKind.Assign)

    def test_tokenize_identifiers(self, new_tokenizer):
        assert new_tokenizer.tokenize("True") == [Token(TokenKind.TruthVal, "True")]
        assert new_tokenizer.tokenize("False") == [Token(TokenKind.TruthVal, "False")]
        assert new_tokenizer.tokenize("test") == [Token(TokenKind.Prep, "test")]

    def test_misc_expressions(self, new_tokenizer):
        identifier_tokens = new_tokenizer.tokenize("A->B")
        assert identifier_tokens[0] == Token(TokenKind.Prep, "A")
        assert identifier_tokens[1] == Token(TokenKind.Impl)
        assert identifier_tokens[2] == Token(TokenKind.Prep, "B")


