"""

## ejercicio uno pre examen

def leerEntero(leyenda, minimo, maximo):
    print("ingrese un valor entre", minimo, "a", maximo)
    entero = int(input(leyenda))
    flag_exit_while = True

    while flag_exit_while:
        if minimo <= entero <= maximo:
            flag_exit_while = False
        else:
            print("parametro invalido, tiene que ser en un rango de", minimo, "a", maximo)
            entero = int(input(leyenda))
    return entero


def leerFecha():
    dia = leerEntero("Ingrese el dia", 1, 31)
    mes = leerEntero("ingrese el mes", 1, 12)
    anio = leerEntero("ingrese el año", 1900, 2018)
    return dia, mes, anio


dia, mes, anio = leerFecha()

print("la fecha es", dia, "/", mes, "/", anio)

"""

## ingresar un valor entero y positivo, informar si el numero tiene raiz exacta
"""
def leerNumeroEnteroPositivo():
    numero = int(input("ingresar un numero entero y positivo"))
    while numero < 0:
        numero = int(input("ingresar un numero entero y positivo"))
    return numero


def numeroRaizExacta(numero):
    count = 1
    isPerfectSquare = False
    while numero > 0:
        numero = numero - count
        if numero == 0:
            isPerfectSquare = True
        count = count + 2
    return isPerfectSquare


def analizarNumeroPerfecto(numero):
    if numeroRaizExacta(numero):
        print("es un numero con raiz perfecta")
    else:
        print("no es un numero con raiz perfecta")


analizarNumeroPerfecto(leerNumeroEnteroPositivo())
"""
## generar dos numeros random simulando la tirada de ruleta
## con uno obtengo el color 1-rojo / 2-negro / 3-verde
## con el otro un numero entre 0 y 36
## calcular en 80 tiradas
## 1 cuantas veces salio la primera docena
## 2 Cuantas veces salio el cero
## 3 cuantas veces salio el negro
## % que salio el rojo

"""
import random


def obtenerColorYnumero():
    return random.randint(1, 3), random.randint(0, 36)


def compararYacumular(valor, comparado, acumulador):
    if valor == comparado:
        return acumulador + 1
    else:
        return acumulador


def compararEntreMinMaxInclusiveYacumular(valor, min, max, acumulador):
    if min <= valor <= max:
        return acumulador + 1
    else:
        return acumulador


def tirarRuletaYgenerarEstadisticas(cantidadDeTiradas):
    primeraDocena = 0
    cantidadCero = 0
    cantidadNegro = 0
    cantidadRojo = 0

    for i in range(0, cantidadDeTiradas + 1):
        color, numero = obtenerColorYnumero()

        primeraDocena = compararEntreMinMaxInclusiveYacumular(numero, 1, 12, primeraDocena)

        cantidadCero = compararYacumular(numero, 0, cantidadCero)

        cantidadNegro = compararYacumular(color, 2, cantidadNegro)

        cantidadRojo = compararYacumular(color, 1, cantidadRojo)

    return primeraDocena, cantidadCero, cantidadNegro, (cantidadRojo / cantidadDeTiradas) * 100


primeraDocena, cantidadCero, cantidadNegro, cantidadRojo = tirarRuletaYgenerarEstadisticas(80)

print(primeraDocena)
print(cantidadCero)
print(cantidadNegro)
print(cantidadRojo)

"""

"""
Desarrollar un programa que lea un número N entero positivo y genere los elementos
correspondientes a la conjetura de Ullman (en honor al matemático S. Ullman), que consiste
en lo siguiente:
Si N es par, dividirlo por 2
Si es impar multiplicarlo por 3 y sumarle 1.
Utilizar este resultado como nuevo número N y repetir el proceso.
Al final se obtendrá el número 1, independientemente del número inicial. Por ejemplo,
cuando el entero inicial es 26 la secuencia queda como 26, 13, 40, 20, 10, 5, 16, 8, 4,
2, 1.
El programa deberá informar también la cantidad de términos obtenidos.
"""

"""
def leerNumeroEnteroPositivo():
    numero = int(input("ingresar un numero entero y positivo"))
    while numero < 0:
        numero = int(input("ingresar un numero entero y positivo"))
    return numero


def generarImpar(numero):
    return (numero * 3) + 1


def generarPar(numero):
    return numero / 2


def operarNumero(numero):
    if numero % 2 == 0:
        return generarPar(numero)
    else:
        return generarImpar(numero)


def generarConjeturaUllman():
    cont = 0
    numero = leerNumeroEnteroPositivo()
    print(numero)
    while numero != 1:
        cont = cont + 1
        numero = operarNumero(numero)
        print(numero)
    print("cantidad de operaciones", cont)


generarConjeturaUllman()
"""
