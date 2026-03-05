from enum import Enum

class TokenKind(Enum):
    Boolean = 0
    Assign = 1
    Prep = 2
    And = 3
    Or = 4
    Not = 5
    Impl = 6
    Iff = 7
    LParen = 8
    RParen = 9
    Error = 10
    EOF = 11

