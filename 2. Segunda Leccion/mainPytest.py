from main import Calculator

def test_isDigit():
    calculator = Calculator()

    assert calculator.isDigit(1) == True
    assert calculator.isDigit(1.0) == True
    assert calculator.isDigit("NotDigit") == False
    assert calculator.isDigit(None) == False

def test_sum():
    calculator = Calculator()

    assert calculator.sum(1, 2, 3) == 6.0
    assert calculator.sum(1.0, 2, 3.5) == 6.5
    assert calculator.sum(1, 2.3, "NonDigit") == 3.3

def test_multiply():
    calculator = Calculator()

    assert calculator.multiply(1, 2, 3) == 6.0
    assert calculator.multiply(1.0, 2, 3.5) == 7.0
    assert calculator.multiply(1, 2.3, "NonDigit") == 2.3

def test_elevate():
    calculator = Calculator()

    assert round(calculator.elevate(2.2, 2), 2) == 4.84
    assert round(calculator.elevate(5, -1), 2) == 0.2
    assert calculator.elevate("NonDigit", 1) == None
    assert calculator.elevate(1, "NonDigit") == None

def test_divide():
    calculator = Calculator()

    assert calculator.divide(2.5, -3) == 2.5/-3
    assert calculator.divide(1, 0) == None
    assert calculator.divide(0, 5) == 0.0
    assert calculator.divide("NonDigit", 1) == None
