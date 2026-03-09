from logtest.tokenizer.token_kinds import TokenKind
from logtest.interpreter.primitives import Primitive

truth_tables = {
    TokenKind.Not: {
        Primitive.false: Primitive.true,
        Primitive.true: Primitive.false,
    },
    TokenKind.Or: {
        (Primitive.false, Primitive.false): Primitive.false,
        (Primitive.true, Primitive.false): Primitive.true,
        (Primitive.false, Primitive.true): Primitive.true,
        (Primitive.true, Primitive.true): Primitive.true,
    },
    TokenKind.And: {
        (Primitive.false, Primitive.false): Primitive.false,
        (Primitive.true, Primitive.false): Primitive.false,
        (Primitive.false, Primitive.true): Primitive.false,
        (Primitive.true, Primitive.true): Primitive.true,
    },
    TokenKind.Impl: {
        (Primitive.false, Primitive.false): Primitive.true,
        (Primitive.true, Primitive.false): Primitive.false,
        (Primitive.false, Primitive.true): Primitive.true,
        (Primitive.true, Primitive.true): Primitive.true,
    },
    TokenKind.Iff: {
        (Primitive.false, Primitive.false): Primitive.false,
        (Primitive.true, Primitive.false): Primitive.false,
        (Primitive.false, Primitive.true): Primitive.false,
        (Primitive.true, Primitive.true): Primitive.true,
    }
}

