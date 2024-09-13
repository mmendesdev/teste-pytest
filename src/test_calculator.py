import pytest
from calculator import calculate

@pytest.mark.parametrize("operation,a,b,expected", [
    ("add", 1, 1, 2),
    ("subtract", 5, 2, 3),
    ("multiply", 3, 3, 9),
    ("divide", 10, 2, 5),
    ("divide", 5, 0, "error")  # Esperando um erro aqui
])
def test_calculate(operation, a, b, expected):
    if expected == "error":
        with pytest.raises(ValueError):
            calculate(operation, a, b)
    else:
        assert calculate(operation, a, b) == expected
