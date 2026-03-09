import pytest

from logtest.interpreter.interpreter import Interpreter
from logtest.interpreter.environment import Environment
from logtest.tokenizer.tokenizer import Tokenizer
from logtest.parser.parser import Parser


@pytest.fixture
def interpreter():
    return Interpreter(Environment())

def tokenize(string):
    return Tokenizer().tokenize(string)

def parse(tokens):
    return Parser().parse(tokens)

def execute_pipeline(string):
    tokens = Tokenizer().tokenize(string)
    ast = Parser().parse(tokens)
    return Interpreter(Environment()).interpret(ast)


class TestInterpreting:
    def test_interpreting_simple_expressions(self):
        assert execute_pipeline("False") == False
        assert execute_pipeline("True") == True

        assert execute_pipeline("-True || False && True") == False
        assert execute_pipeline("False || (True && False)") == False
        assert execute_pipeline("True -> False <-> True") == False
        
        
    def test_interpreting_variables(self, interpreter):
        i = interpreter

        assert i.interpret(parse(tokenize("A=True"))) == True
        assert i.interpret(parse(tokenize("A"))) == True
        assert i.interpret(parse(tokenize("A=False"))) == False
        assert i.interpret(parse(tokenize("A"))) == False

        assert i.interpret(parse(tokenize("A || True"))) == True


