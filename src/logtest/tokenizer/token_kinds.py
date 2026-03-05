from enum import Enum

class TokenKind(Enum):
    Identifier = 0
    Assign = 1
    And = 2
    Or = 3
    Not = 4
    Impl = 5
    Iff = 6
    LParen = 7
    RParen = 8
    Error = 9
    EOF = 10

