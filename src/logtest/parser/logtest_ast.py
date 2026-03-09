from dataclasses import dataclass

from logtest.tokenizer.tokens import Token
from logtest.tokenizer.token_kinds import TokenKind


@dataclass
class AST_Node:
    def __str__(self) -> str:
        pass


    def dump(self, depth: int=0) -> None:
        pass


@dataclass
class AST_TerminalNode(AST_Node):
    value: str | bool

    def __str__(self) -> str:
        return f"TerminalNode({self.value})"


    def dump(self, depth: int=0) -> None:
        print(depth*"    " + self.__str__())


@dataclass
class AST_UnaryNode(AST_Node):
    op: TokenKind
    operand: AST_Node

    def __str__(self):
        return f"UnaryNode({self.op})"


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


    def dump(self, depth: int=0) -> None:
        print(depth*"    " + self.__str__())
        self.left.dump(depth+1)
        self.right.dump(depth+1)

