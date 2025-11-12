import pytest
import calculadora

## Testa as funcoes da calculadora

## ---- SOMA ----
def test_soma():
    assert calculadora.soma(2, 3) == 5

def test_soma_com_numero_negativo():
    assert calculadora.soma(-1, -5) == -6

def test_soma_float():
    assert calculadora.soma(2.5, 3.1) == pytest.approx(5.6)

## ---- SUBTRAIR ----
def test_subtrair():
    assert calculadora.subtrair(5, 3) == 2

def test_subtrair_com_numero_negativo():
    assert calculadora.subtrair(-1, -5) == 4

def test_subtrair_float():
    assert calculadora.subtrair(5.5, 2.2) == pytest.approx(3.3)

## ---- MULTIPLICAR ----
def test_multiplicar():
    assert calculadora.multiplicar(4, 5) == 20

def test_multiplicar_um_numero_negativo():
    assert calculadora.multiplicar(4, -5) == -20

def test_multiplicar_dois_numeros_negativos():
    assert calculadora.multiplicar(-4, -5) == 20

def test_multiplicar_por_zero():
    assert calculadora.multiplicar(0, 5) == 0

def test_multiplicar_float():
    assert calculadora.multiplicar(2.5, 4.0) == pytest.approx(10.0)

## ---- DIVIDIR ----
def test_dividir():
    assert calculadora.dividir(10, 2) == 5

def test_dividir_com_numero_negativo():
    assert calculadora.dividir(10, -2) == -5

def test_dividir_dois_numeros_negativos():
    assert calculadora.dividir(-10, -2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        calculadora.dividir(10, 0)
        
def test_dividir_float():
    assert calculadora.dividir(5.5, 2.0) == pytest.approx(2.75)