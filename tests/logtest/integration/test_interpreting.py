import pytest

from logtest.interpreter.primitives import Primitive
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
        assert execute_pipeline("False") == Primitive.false
        assert execute_pipeline("True") == Primitive.true

        assert execute_pipeline("-True || False && True") == Primitive.false
        assert execute_pipeline("False || (True && False)") == Primitive.false
        assert execute_pipeline("True -> False <-> True") == Primitive.false
        
        
    def test_interpreting_variables(self, interpreter):
        i = interpreter

        assert i.interpret(parse(tokenize("A=True"))) == Primitive.true
        assert i.interpret(parse(tokenize("A"))) == Primitive.true
        assert i.interpret(parse(tokenize("A=False"))) == Primitive.false
        assert i.interpret(parse(tokenize("A"))) == Primitive.false

        assert i.interpret(parse(tokenize("A || True"))) == Primitive.true


