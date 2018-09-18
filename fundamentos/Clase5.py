import random

# generar un numero aleatorio entre 100 y 4000,
# informar si el valor generado pertenece a la sucesion de fibonacci
# y en que posicion esta

"""
# init values
sinceRandomInt = 100
endRandomInt = 4000

varFibonacciA = 0
varFibonacciB = 1
varFibonacciC = 0

positionFibonacci = 2
flagExitWhile = True
# init values

numeroActual = random.randint(sinceRandomInt, endRandomInt)
while flagExitWhile:

    varFibonacciC = varFibonacciA + varFibonacciB
    varFibonacciA = varFibonacciB
    varFibonacciB = varFibonacciC
    positionFibonacci = positionFibonacci + 1

    if varFibonacciB == numeroActual:
        flagExitWhile = False
        print("El numero generado es: ", numeroActual, "pertenece a fibonacci y su posicion es: ", positionFibonacci)

    if numeroActual < varFibonacciB:
        flagExitWhile = False
        print("el numero generado es: ", numeroActual, " y no pertenece a la sucesion de fibocacci")
"""

# dada la serie 2^n y 3^n-1
# generar un numero aleatorio entre 1 y 6562 eh informar si esta mas cerca del 2 y 3

"""
# init values
sinceRandomInt = 1
endRandomInt = 6562
potency = 2
flagExit = True
# init values

actualNumber = random.randint(sinceRandomInt, endRandomInt)

while flagExit:

    twoPotency = 2 ** (potency + 1)
    threePotency = 3 ** potency

    # si el numero generado esta entre 1 y 7 debe de salir ya que no se puede comparar
    if actualNumber < 8:
        flagExit = False
        print("el numero", actualNumber, " no se puede comparar entre", twoPotency, "y", threePotency)

    if twoPotency <= actualNumber <= threePotency:
        flagExit = False
        intervale = str(twoPotency) + "<=" + str(actualNumber) + "<=" + str(threePotency)
        if (actualNumber - twoPotency) < (threePotency - actualNumber):
            print("el numero esta cercano a 2^n", intervale)
        elif (actualNumber - twoPotency) > (threePotency - actualNumber):
            print("el numero esta cercano a 3^n", intervale)
        else:
            print("el numero se encuentra en el medio de ambas potencias", intervale)

    potency = potency + 1
"""

# generar un simon dice de 8 numero y 4 rondas, limpiando pantalla con un while


# ingresar dos numeros de dos digitos cada uno, efectual su producto e informar si el numero
# obtenido es un numero vampiro(cantidad par de digitos, los digitos son los mismos que los colmillos pero en cualquier orden)
# 21x60 = 1260, los colmillos no pueden terminar en cero al mismo tiempo
"""
numeroA = int(input("ingrese un numero A de dos digitos"))
numeroB = int(input("ingrese un numero B de dos digitos"))

if numeroA <= 99 and numeroB <= 99:
    
    numeroMultiplicado = str(numeroA * numeroB)
    
    condition1 = numeroMultiplicado.find(str(numeroA)[0]) != -1
    condition2 = numeroMultiplicado.find(str(numeroA)[1]) != -1
    condition3 = numeroMultiplicado.find(str(numeroB)[0]) != -1
    condition4 = numeroMultiplicado.find(str(numeroB)[1]) != -1
    
    condition5 = int(numeroMultiplicado[2]) != 0 or int(numeroMultiplicado[3]) != 0
    if len(numeroMultiplicado) == 4:
        if condition1 and condition2 and condition3 and condition4 and condition5:
            print(numeroMultiplicado, "es un numero vampiro")
        else:
            print(numeroMultiplicado, "no es un numero vampiro")
    else:
        print("la cantidad de digitos de", numeroMultiplicado, "es mas grande que la cantidad de digitos de", numeroA, numeroB)
            
else:
    print("ingreso valores mayores a dos digitos", numeroB, numeroA)
"""

## no funciona, falta desarrollo

numeroA = 99
numeroB = 99

if numeroA <= 99 and numeroB <= 99:

    numeroMultiplicado = numeroA * numeroB
    numeroAprimero = numeroA // 10
    numeroAsegundo = numeroA % 10
    numeroBprimero = numeroB // 10
    numeroBsegundo = numeroB % 10

    numeroMultiplicadoCuarto = numeroMultiplicado % 10
    numeroMultiplicadoTercero = (numeroMultiplicado % 100) // 10
    numeroMultiplicadoSegundo = (numeroMultiplicado % 1000) // 100
    numeroMultiplicadoPrimero = (numeroMultiplicado % 10000) // 1000

    primeraCondicion = numeroAprimero == numeroMultiplicadoPrimero or numeroAprimero == numeroMultiplicadoSegundo or numeroAprimero == numeroMultiplicadoTercero or numeroAprimero == numeroMultiplicadoCuarto
    segundaCondicion = numeroAsegundo == numeroMultiplicadoPrimero or numeroAsegundo == numeroMultiplicadoSegundo or numeroAsegundo == numeroMultiplicadoTercero or numeroAsegundo == numeroMultiplicadoCuarto
    terceraCondicion = numeroBprimero == numeroMultiplicadoPrimero or numeroBprimero == numeroMultiplicadoSegundo or numeroBprimero == numeroMultiplicadoTercero or numeroBprimero == numeroMultiplicadoCuarto
    cuartaCondicion = numeroBsegundo == numeroMultiplicadoPrimero or numeroBsegundo == numeroMultiplicadoSegundo or numeroBsegundo == numeroMultiplicadoTercero or numeroBsegundo == numeroMultiplicadoCuarto
    quintaCondicion = numeroMultiplicadoTercero != 0 or numeroMultiplicadoCuarto != 0

    if primeraCondicion and segundaCondicion and terceraCondicion and cuartaCondicion or quintaCondicion:
        print(numeroMultiplicado, "es un numero vampiro")
    else:
        print(numeroMultiplicado, "no es un numero vampiro")

else:
    print("ingreso valores mayores a dos digitos", numeroB, numeroA)
