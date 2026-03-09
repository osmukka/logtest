from logtest.tokenizer.token_kinds import TokenKind
from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode, AST_UnaryNode, AST_BinaryNode
from logtest.interpreter.environment import Environment
from logtest.interpreter.primitives import Primitive
from logtest.interpreter.tables import truth_tables


class Interpreter:
    def __init__(self, env: Environment) -> None:
        self._env = env


    def _eval(self, ast: AST_Node) -> AST_TerminalNode:
        if isinstance(ast, AST_TerminalNode):
            return self._eval_terminal(ast)

        elif isinstance(ast, AST_UnaryNode):
            return self._eval_unary(ast)

        elif isinstance(ast, AST_BinaryNode):
            return self._eval_binary(ast)


    def _eval_terminal(self, ast: AST_TerminalNode) -> AST_TerminalNode:
        if type(ast.value) == Primitive:
            return ast
        return AST_TerminalNode(self._env.get_variable(ast.value))


    def _eval_unary(self, ast: AST_UnaryNode) -> AST_TerminalNode:
        argument = self._eval(ast.operand).value
        return AST_TerminalNode(truth_tables[ast.op][argument])


    def _eval_binary(self, ast: AST_BinaryNode) -> AST_TerminalNode:
        if ast.op is TokenKind.Assign:
            if not isinstance(ast.left, AST_TerminalNode):
                    raise ValueError(f"Left hand side of assign must be AST_TerminalNode, found {type(ast.left)}")
            right = self._eval(ast.right)
            if not isinstance(ast.right, AST_TerminalNode):
                raise ValueError(f"Right hand side of assign must be AST_TerminalNode, found {type(ast.right)}")
            self._env.set_variable(ast.left.value, self._env.get_primitive_name(right.value))
            return right

        else:
            left = self._eval(ast.left).value
            right = self._eval(ast.right).value
            arguments = (left, right)
            return AST_TerminalNode(truth_tables[ast.op][arguments])



    def interpret(self, ast: AST_Node):
        return self._eval(ast).value

        return return_value.value


