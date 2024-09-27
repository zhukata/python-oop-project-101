from validator.base_validator import Validator


def test_number_validator():
    v = Validator()
    schema = v.number()
    assert schema.is_valid(None)


def test_number_required():
    v = Validator()
    schema = v.number()
    schema.required()
    assert not schema.is_valid(None)
    assert schema.is_valid(7)


def test_number_positive():
    v = Validator()
    schema = v.number()
    assert schema.positive().is_valid(10) # True


# def test_number_range():
#     v = Validator()
#     schema = v.number()
#     schema.range(-5, 5)
#     # валидатор positive все еще "включен"
#     assert not schema.is_valid(-5) # False
#     assert schema.is_valid(5) # True
