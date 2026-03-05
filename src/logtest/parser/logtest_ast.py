from dataclasses import dataclass
from typing import Any

from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind
from logtest.interpreter.environment import Environment


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


@dataclass
class AST_Node:
    def __str__(self) -> str:
        pass

    def eval(self, env: Environment) -> Any:
        pass

    def dump(self, depth: int=0) -> None:
        pass


@dataclass
class AST_TerminalNode(AST_Node):
    value: str | bool

    def __str__(self) -> str:
        return f"TerminalNode({self.value})"

    def eval(self, env: Environment) -> AST_Node:
        if isinstance(self.value, bool):
            return AST_TerminalNode(self.value)
        else:
            return AST_TerminalNode(env.get_variable(self.value))

    def dump(self, depth: int=0) -> None:
        print(depth*"    " + self.__str__())


@dataclass
class AST_UnaryNode(AST_Node):
    op: TokenKind
    operand: AST_Node

    def __str__(self):
        return f"UnaryNode({self.op})"

    def eval(self, env: Environment) -> AST_Node:
        argument = self.operand.eval(env).value
        table = truth_tables[self.op]
        result = table[argument]

        return AST_TerminalNode(result)

    def dump(self, depth: int=0) -> None:
        print(depth*"    " + self.__str__())
        self.operand.dump(depth+1)


@dataclass
class AST_BinaryNode(AST_Node):
    left: AST_Node
    op: TokenKind
    right: AST_Node
    
    def __str__(self) -> str:
        return f"BinaryNode({self.op})"

    def eval(self, env: Environment) -> AST_TerminalNode:
        arguments = (self.left.eval(env).value, self.right.eval(env).value)
        table = truth_tables[self.op]
        result = table[arguments]

        return AST_TerminalNode(result)

    def dump(self, depth: int=0) -> None:
        print(depth*"    " + self.__str__())
        self.left.dump(depth+1)
        self.right.dump(depth+1)






