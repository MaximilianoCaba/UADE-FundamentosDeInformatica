import ejercicios.SequentialStructure as sequentialStructure

# \n
# numero1 = int(input("ingrese numero 1: \n"))
# numero2 = int(input("ingrese numero 2: \n"))
# print("la suma es: ", (numero1 + numero2), "\n")
# print("la resta es: ", (numero1 - numero2), "\n")


"""ventas = [int(x) for x in input("Ingrese una lista de ventas separadas por coma").split(",")]

print(sequentialStructure.calcularSalario(1, ventas))
"""

# CLASE 2

"""
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")


print(numbers_to_strings(0))
"""
"""
num1 = int(input("ingrese la primera nota: "))
num2 = int(input("ingrese la segunda nota: "))

if num1 >= 7:
    if num2 >= 7:
        print("promociono")
    else:
        print("no promociono")
else:
    print("no promociono")

print("programa terminado")
"""

# ingresar 3 valores A B C que corresponden a los lados de un triangulo
# 3 = equilatero
# 2 = isosles
# ninguno = escaleno?
# informar que tipo de traingulo es

"""
numA = int(input("ingrese el lado A: "))
numB = int(input("ingrese el lado B: "))
numC = int(input("ingrese el lado C: "))

if numA + numB > numC and numB + numC > numA and numA + numC > numB:
    if numA == numB and numB == numC:
        print("ES EQUILATERO")
    elif numA != numB and numB != numC and numA != numC:
        print("ES ESCALENO")
    else:
        print("ES ISOSELES")
else:
    print("no es un triangulo")

"""

"""
num1 = int(input("ingrese un numero"))
num2 = int(input("ingrese otro numero"))
num3 = int(input("ingrese otro numero"))
if num1 == num2 and num2 == num3:
    print("equilatero")
if num1 == num3 or num1 == num2 or num2 == num3:
    print("isoseles")
if num1 != num2 and num2 != num3 and num1 != num3:
    print("escaleno")
"""

"""
count = 0
while count < 5:
    print count
    count += 1  # This is the same as count = count + 1
"""

"""
primes = [2,3,5,7]
for prime in primes:
    print prime
"""

# ingresar 30 valores que corresponden al total de gastos diarios a lo largo de un mes
# informar cual fue el total mensual gastado
# cual fue el mayor importe que tuve en el mes

"""
num1 = 0
cont = 0
valormaximo = 0
while cont < 30:
    valoractual = int(input("ingrese el gasto"))
    cont = cont + 1
    num1 = num1 + valoractual
    if valormaximo <= valoractual:
        valormaximo = valoractual

print(num1)
print(valormaximo)

# ingresar los gastos habidos durante un mes e informar el total
#
"""

import os

import time

print("hola")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')