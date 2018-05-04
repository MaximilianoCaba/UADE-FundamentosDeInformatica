import random

# 1 - ingresar un valor positivo menor a 100, controlar que se asi eh informar si es par o impar

# 2 - ingresar un valor menor a 500, informar si es un numero primo (divisible por uno y por si mismo)

# 3 - ingresar un numero positivo e informar si es un numero abundante (suma de los divisores da mas que el numero 12)
#     | deficiente (opuesto abundante)| perfecto (suma divisores sin el numero da el numero 6)

# 4 - dada las variables A y B, con valores iniciales 0 y 1 respectivamente, generar la serie de fibonnachi
#     hasta el elemento el numero 20 cada componente de la serie se obtiene por la suma de los dos anteriores

# 5 - ingresar un numero menor a 10 positivo eh informar si es un numero curioso (numero elevado al cuadrado
#     tiene al numero como ultimo digito 5elevado2 25)

# 6 - ingresar un numero positivo y verificar un numero oblongo (producto de dos numero naturales consecutivos, 30 -> 5x6)

# 7 - ingresar un valor entero y positivo eh informar si tiene raiz cuadrada exacta

# 9 | 1
# 8 | 3
# 5 | 5
# 0

# 16 | 1
# 15 | 3
# 12 | 5
# 7  | 7
# 0  |

""" Ejercicio 1
numero = int(input("ingresar un numero menor a 100 positivo"))

while numero < 0 or numero > 100:
    numero = int(input("ingresar un numero menor a 100 positivo"))

if (numero % 2) == 0:
    print("el numero es par")
else:
    print("el numero es impar")
"""

""" Ejercicio 2
numero = int(input("ingresar un numero menor a 500"))

while numero > 500:
    numero = int(input("ingresar un numero menor a 500"))

ifNumberIsCousin = True
count = 2
while count < numero:
    if (numero % count) == 0:
        ifNumberIsCousin = False
    count = count + 1

if ifNumberIsCousin:
    print("el numero es primo")
else:
    print("el numero no es primo")
"""

"""
numero = int(input("ingresar un numero positivo"))

while numero < 0:
    numero = int(input("ingresar un numero positivo"))

divisorSum = 0
count = 1
while count < numero:
    if (numero % count) == 0:
        divisorSum = divisorSum + count
    count = count + 1

if divisorSum > numero:
    print("abundante")

if divisorSum < numero:
    print("deficiente")

if divisorSum == numero:
    print("perfecto")
"""

""" ejercicio 4
varA = 0
varB = 1
varC = 0

print("la sucesion de fibonachi es: ")
print(varA)
print(varB)
while varC <= 20:
    varC = varA + varB
    varA = varB
    varB = varC
    if varB <= 20:
        print(varB)
"""
"""
numero = int(input("ingresar un numero positivo menor a 10"))

while numero < 0 or numero > 10:
    numero = int(input("ingresar un numero positivo menor a 10"))

originalNumero = str(numero)
numero = numero * numero
numeroString = str(numero)[-1]

if numeroString == originalNumero:
    print("es un numero curioso")
else:
    print("no es un numero curioso")
"""
"""
numero = int(input("ingresar un numero positivo"))

while numero < 0:
    numero = int(input("ingresar un numero positivo"))

count = 0
isOblongo = False

while count < numero:
    if (count * (count + 1)) == numero:
        isOblongo = True
    count = count + 1

if isOblongo:
    print("el numero es oblongo")
else:
    print("no es un numero oblongo")
"""
"""ejercicio 7
numero = int(input("ingresar un numero entero y positivo"))

while numero < 0:
    numero = int(input("ingresar un numero entero y positivo"))

count = 1
isPerfectSquare = False
while numero > 0:
    numero = numero - count
    if numero == 0:
        isPerfectSquare = True
    count = count + 2

if isPerfectSquare:
    print("es un numero con raiz perfecta")
else:
    print("no es un numero con raiz perfecta")
"""

"""
random.randint(init, init) -> numero entero
random.uniform(1,10) -> numero real
random.random() -> numero entre 0<random<1

"""

# simular la tirada de un dado 20 veces, informar, cuantas veces salio el numero 5

"""
count = 0
cantNumberFive = 0

while count <= 20:
    if random.randint(1, 6) == 5:
        cantNumberFive = cantNumberFive + 1
    count = count + 1

print("la cantidad de numero 5 obtenidos en 20 jugadas es: " + str(cantNumberFive))
"""
# arrojar la bola de la ruleta 100 veces, por fin de proceso informar,
# cuantas veces salio un valor de la segunda docena
# cuantas veces salio el cero
# porcentaje de valor que salio de la primera docena
# cual fue el valor maximo en la serie

"""
count = 0
cantPrimeraDocena = 0
cantSegundaDoncena = 0
cantCero = 0
valorMaximo = 0
while count < 100:
    numeroActual = random.randint(0, 36)
    if 1 <= numeroActual <= 12:
        cantPrimeraDocena = cantPrimeraDocena + 1
    if 13 <= numeroActual <= 24:
        cantSegundaDoncena = cantSegundaDoncena + 1
    if numeroActual == 0:
        cantCero = cantCero + 1
    if valorMaximo < numeroActual:
    
        valorMaximo = numeroActual
    count = count + 1
print("cantidad de veces que salio un valor de la segunda docena: ", cantSegundaDoncena)
print("porcentaje de veces que salio un valor de la primera docena: ", (cantPrimeraDocena * 100) / count)
print("cantidad de veces que salio el cero: ", cantCero)
print("valor maximo en 100 tiros: ", valorMaximo)
"""


