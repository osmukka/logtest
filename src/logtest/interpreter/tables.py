from logtest.tokenizer.token_kinds import TokenKind

truth_tables = {
    TokenKind.Not: {
        False: True,
        True: False,
    },
    TokenKind.Or: {
        (False, False): False,
        (True, False): True,
        (False, True): True,
        (True, True): True,
    },
    TokenKind.And: {
        (False, False): False,
        (True, False): False,
        (False, True): False,
        (True, True): True,
    },
    TokenKind.Impl: {
        (False, False): True,
        (True, False): False,
        (False, True): True,
        (True, True): True,
    },
    TokenKind.Iff: {
        (False, False): False,
        (True, False): False,
        (False, True): False,
        (True, True): True,
    }
}

