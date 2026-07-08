from src.main import somar, multiplicar, dividir

def test_soma():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_multiplicacao():
    assert multiplicar(2, 3) == 6
    assert multiplicar(4, 0) == 0

def test_somamultiplicada():
    assert somar(2, multiplicar(3, 2)) == 8
    assert somar(0, multiplicar(6, 0)) == 0

def test_divisao():
    assert dividir(10, 2) == 5
    assert dividir(20, 2) == 10