from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode
from logtest.interpreter.environment import Environment


class Interpreter:
    def __init__(self, env: Environment) -> None:
        self.env = env

    def interpret(self, ast: AST_Node):
        return_value = ast.eval(self.env)

        match type(return_value):
            case AST_TerminalNode:
                if isinstance(return_value.value, bool):
                    return return_value.value
                else:
                    return self.env.get_variable(return_value.value)

