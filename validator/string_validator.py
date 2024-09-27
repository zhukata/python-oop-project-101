class StringValidator():
    def __init__(self):
        self.state = None
        self.current_value = None

    def get_state(self):
        return self.state
    
    def is_valid(self, value):
        if self.state == 'required':
            if not value:
                return False

        elif self.state == 'contains':
            if self.current_value in value:
                return True
            else:
                return False

        elif self.state == 'min_len':
            if self.current_value <= len(value):
                return True
            else:
                return False

        return True

    def required(self):
        self.state = 'required'
        return self
    
    def contains(self, value):
        self.state = 'contains'
        self.current_value = value
        return self

    def min_len(self, value):
        self.state = 'min_len'
        self.current_value = value
        return self