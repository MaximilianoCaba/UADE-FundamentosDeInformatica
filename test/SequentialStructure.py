import ejercicios.SequentialStructure as sequentialStructure

"""Desarrollar un programa que permita ingresar dos números enteros A y B a través
del teclado. Imprimir su suma y su diferencia."""


def test_rest_two_number():
    resutRest = sequentialStructure.rest(2, 2)
    assert resutRest == 0
    print("resultado de la resta: " + str(resutRest))


def test_sum_two_number():
    resultSum = sequentialStructure.sum(2, 2)
    assert resultSum == 4
    print("resultado de la Suma: " + str(resultSum))
