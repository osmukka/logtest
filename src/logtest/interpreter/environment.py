from logtest.interpreter.primitives import Primitive


class Environment:
    def __init__(self) -> None:
        self._primitives = {
            "False": Primitive.false,
            "True": Primitive.true
        }
        self._primitive_names = {
            Primitive.false: "False",
            Primitive.true: "True"
        }
        self._variables = {
            "True": "True",
            "False": "False"
        }


    def get_primitive(self, name: str) -> Primitive | None:
        return self._primitives.get(name)


    def get_primitive_name(self, primitive: Primitive) -> str:
        return self._primitive_names[primitive]


    def get_variable(self, name: str) -> str:
        if name not in self._variables:
            raise ValueError(f"Variable {name} is not set")
        primitive_name = self._variables[name]
        return self._primitives[primitive_name]


    def set_variable(self, name: str, value: str) -> None:
        if name in self._primitives:
            raise ValueError("Values of True and False cannot be changed")

        primitive_name = self._variables[value]
        self._variables[name] = primitive_name


    def reset_variable(self, name: str) -> None:
        if name in self._variables:
            raise ValueError("Variables True and False cannot be reset")

