"""
range(20, 6, -1)
20 -> 7"""

# El factorial de un número entero N mayor que cero se define como el producto de todos los
# enteros X tales que 0 < X <= N. Desarrollar un programa para calcular el factorial de un
# número dado. Deberán rechazarse las entradas inválidas (menores que 0).

# 4! = 1x2x3x4 = 24

"""
numero = 0
isValidNumber = False
factorial = 1

while not isValidNumber:
    numero = int(input("ingrese valor mayor a cero y menor a 10"))
    if 0 < numero < 11:
        isValidNumber = True

for i in range(1, (numero + 1)):
    factorial = i * factorial

print("el factorial de ",numero, "es ", factorial)
"""

# Una empresa cuenta con 100 empleados, divididos en tres categorías A, B y C. Por cada
# empleado se lee su legajo, categoría y salario. Se solicita elaborar un informe que contenga:

# 1 Importe total de salarios pagados por la empresa.
# 2 Cantidad de empleados que ganan más de $20000.
# 3 Cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”.
# 4 Legajo del empleado que más gana.
# 5 Sueldo más bajo.
# 6 Importe total de sueldos por cada categoría.
# 7 Salario promedio

"""
import random

salarioTotal = 0
empleadosSueldosVeinteMil = 0
empleadosCincoMilCatC = 0
legajoEmpleadoMasGana = 0
sueldoMasAlto = 0
sueldoMasBajo = 99999999
totalCategoriaA = 0
totalCatetoriaB = 0
totalCategoriaC = 0
salarioPromedio = 0

for i in range(1, 101):
    # legajo = int(print("ingrese el numero de legajo"))
    legajo = random.randint(0, 9999999)
    # salario = int(print("ingrese el salario"))
    salario = random.randint(2500, 25000)
    # categoria = str(print("Ingrese la categoria A B o C"))
    categoria = random.choice("ABC")

    # 1
    salarioTotal = salarioTotal + salario

    # 2
    if salario >= 20000:
        empleadosSueldosVeinteMil = empleadosSueldosVeinteMil + 1

    # 3
    if salario <= 5000 and categoria == "C":
        empleadosCincoMilCatC = empleadosCincoMilCatC + 1

        # 4
    if salario > sueldoMasAlto:
        sueldoMasAlto = salario
        legajoEmpleadoMasGana = legajo

    # 5
    if salario < sueldoMasBajo:
        sueldoMasBajo = salario

    # 6
    if categoria == "A":
        totalCategoriaA = totalCategoriaA + salario

    if categoria == "B":
        totalCatetoriaB = totalCatetoriaB + salario

    if categoria == "C":
        totalCategoriaC = totalCategoriaC + salario

salarioPromedio = salarioTotal / 100

print("#1 cantidad total a pagar=", salarioTotal)
print("#2 empleados que ganan mas de 20000=", empleadosSueldosVeinteMil)
print("#3 empleado < 5000 y categoria C=", empleadosCincoMilCatC)
print("#4 legajo empleado que mas gana=", legajoEmpleadoMasGana)
print("#5 sueldo mas bajo=", sueldoMasBajo)
print("#6 categoria A=", totalCategoriaA, "categoria B=", totalCatetoriaB, "categoria C=", totalCategoriaC)
print("#7 salario promedio=", salarioPromedio)
"""


def calcular(n1=1):
    return n1


print(calcular(3))
