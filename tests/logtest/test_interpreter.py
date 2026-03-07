import pytest

from logtest.interpreter.interpreter import Interpreter
from logtest.interpreter.environment import Environment
from logtest.tokenizer.tokenizer import Tokenizer
from logtest.parser.parser import Parser

def interpret(string: str):
    tokens = Tokenizer().tokenize(string)
    ast = Parser().parse(tokens)
    return Interpreter(Environment()).interpret(ast)



class TestInterpreter:
    def test_interpreting_terminals(self):
        assert interpret("True") == True
        assert interpret("False") == False

    def test_interpreting_not(self):
        assert interpret("-False") == True
        assert interpret("-True") == False

    def test_interpreting_or(self):
        assert interpret("False || False") == False
        assert interpret("True || False") == True
        assert interpret("False || True") == True
        assert interpret("True || True") == True

    def test_interpreting_and(self):
        assert interpret("False && False") == False
        assert interpret("True && False") == False
        assert interpret("False && True") == False
        assert interpret("True && True") == True

    def test_interpreting_impl(self):
        assert interpret("False -> False") == True
        assert interpret("True -> False") == False
        assert interpret("False -> True") == True
        assert interpret("True -> True") == True

    def test_interpreting_iff(self):
        assert interpret("False <-> False") == False
        assert interpret("True <-> False") == False
        assert interpret("False <-> True") == False
        assert interpret("True <-> True") == True

    def test_setting_variable(self):
        assert interpret("A=True") == True

    def test_accessing_variable(self):
        interpreter = Interpreter(Environment())
        tokens = Tokenizer().tokenize("A=False")
        ast = Parser().parse(tokens)
        assert interpreter.interpret(ast) == False

        tokens = Tokenizer().tokenize("A")
        ast = Parser().parse(tokens)
        assert interpreter.interpret(ast) == False


    def test_accessing_unbound_variable(self):
        with pytest.raises(ValueError):
            interpret("a")

    def test_setting_true_and_false(self):
        with pytest.raises(ValueError):
            interpret("True=False")
        with pytest.raises(ValueError):
            interpret("False=True")


