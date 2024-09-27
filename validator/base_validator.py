from validator.number_validator import NumberValidator
from validator.string_validator import StringValidator


class Validator():
    def __init__(self) -> None:
        self.validator_type = StringValidator

    def string(self):
        return StringValidator()
    
    def number(self):
        return NumberValidator()

