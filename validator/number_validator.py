class NumberValidator():
    def __init__(self) -> None:
        self.state = None
        self.current_value = None

    def is_valid(self, value):
        if self.state == 'required':
            if not value:
                return False

        elif self.state == 'positive':
            if value > 0:
                return True
            else:
                return False

        elif self.state == 'range':
            x, y = self.current_value
            if value in range(x, y):
                return True
            else:
                return False

        return True

    def required(self):
        self.state = 'required'
        return self
    
    def positive(self):
        self.state = 'positive'
        return self

    def range(self, value1, value2):
        self.state = 'range'
        self.current_value = (value1, value2)
        return self