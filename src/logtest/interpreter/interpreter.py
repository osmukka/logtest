from logtest.parser.logtest_ast import AST_Node, AST_TerminalNode


class Interpreter:
    def __init__(self) -> None:
        pass

    def interpret(self, ast: AST_Node):
        return_value = ast.eval()

        match type(return_value):
            case AST_TerminalNode:
                return return_value.value

