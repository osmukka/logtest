from logtest.tokenizer.token_kinds import TokenKind
from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode, AST_BinaryNode
from logtest.interpreter.environment import Environment


class Interpreter:
    def __init__(self, env: Environment) -> None:
        self.env = env


    def interpret(self, ast: AST_Node):
        return_value = ast.eval(self.env)

        if isinstance(return_value, AST_TerminalNode):
            if isinstance(return_value.value, bool):
                return return_value.value
            else:
                return self.env.get_variable(return_value.value)

        elif isinstance(return_value, AST_BinaryNode):
                if return_value.op is not TokenKind.Assign:
                    raise ValueError(f"Expected TokenKind.Assign as return value, found {return_value.op}")

                if not isinstance(return_value.left, AST_TerminalNode):
                    raise ValueError(f"Left hand side of assign must be AST_TerminalNode, found {type(return_value.left)}")
                if not isinstance(return_value.right, AST_TerminalNode):
                    raise ValueError(f"Right hand side of assign must be AST_TerminalNode, found {type(return_value.right)}")

                variable_name = return_value.left.value
                variable_value = return_value.right.value
                try:
                    self.env.set_variable(variable_name, variable_value)
                    return variable_value
                except ValueError as e:
                    raise e

