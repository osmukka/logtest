from logtest.tokenizer.tokenizer import Tokenizer
from logtest.tokenizer.token_kinds import TokenKind
from logtest.tokenizer.tokens import Token
from logtest.parser.parser import Parser
from logtest.interpreter.interpreter import Interpreter
from logtest.interpreter.environment import Environment

def main():
    interpreter = Interpreter(Environment())
    while True:
        string = input("> ")

        # Tokenize the string.
        tokens = Tokenizer().tokenize(string)
        has_error_token = False
        for token in tokens:
            if token.kind is TokenKind.Error:
                value, index = token.value
                print(f"Unexpected token '{value}' at index {index}")
                has_error_token = True
        if has_error_token:
            continue

        # Generate ast from the list of tokens.
        try:
            ast = Parser().parse(tokens)
        except ValueError as e:
            print("Parse error", str(e))
            continue

        # Interpret the ast.
        try:
            result = interpreter.interpret(ast)
        except ValueError as e:
            print("Interpreter error:", str(e))
            continue
        print(result)


if __name__ == "__main__":
    main()
