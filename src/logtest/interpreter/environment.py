


class Environment:
    def __init__(self) -> None:
        self.invariables = {"True", "False"}
        self.variables = {
            "True": True,
            "False": False
        }


    def get_variable(self, name: str) -> str:
        if name not in self.variables:
            raise ValueError(f"Variable {name} is not set")


    def set_variable(self, name: str, value: str) -> None:
        if name in self.invariables:
            raise ValueError("Values of True and False cannot be changed")

        self.variables[name] = self.get_variable(value)


    def reset_variable(self, name: str) -> None:
        if name in self.variables:
            raise ValueError("Variables True and False cannot be reset")

