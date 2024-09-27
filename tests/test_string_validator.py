from validator.base_validator import Validator


def test_string_validator():
    v = Validator()
    schema = v.string()
    schema2 = v.string()
    assert schema != schema2
    assert schema.is_valid('')


def test_string_required():
    v = Validator()
    schema = v.string()
    schema.required()
    schema2 = v.string()
    assert schema2.is_valid(None)
    assert not schema.is_valid('')
    assert schema.is_valid('hexlet')


def test_string_contains():
    v = Validator()
    schema = v.string()
    assert schema.contains('what').is_valid('what does the fox say')
    assert not schema.contains('whatthe').is_valid('what does the fox say')


def test_string_min_len():
    v = Validator()
    schema = v.string()
    assert v.string().min_len(10).min_len(4).is_valid('Hexlet')
    assert not schema.min_len(3).is_valid('HE')
