""" int() transforma un string a int / str() transforma un string a int"""
import datetime

pi: 3.141592653589793


def sum(enteroA, enteroB):
    return enteroA + enteroB


def rest(enteroA, enteroB):
    return enteroA - enteroB


# ejercicio 4
def superficieCirculo(radio):
    return pi * (radio * 2)


def perimetroCircunferencia(diametro):
    return pi * diametro


def superficieEsfera(radio):
    return 4 * pi * (radio * 2)


def volumenEsfera(radio):
    return (4 / 3) * pi * (radio * 3)


# ejercicio 5
def edadADias(edad):
    return edad * 365


# ejercico 6
# 1 pie = 12 pulgadas
# 1 yarda = 3 pies
# 1 pulgada = 2,54 cm.
# 1 metro = 100 cm.

def transformarCentimetros(centimetros):
    centimetroAmetros = centimetros / 100
    centimetroApulgadas = centimetros / 2.54
    pulgadaApie = centimetroApulgadas * 12
    pieAyarda = pulgadaApie * 3

    return {
        "metros": centimetroAmetros,
        "pulgadas": centimetroApulgadas,
        "pie": pulgadaApie,
        "yarda": pieAyarda
    }


# ejercicio 7
def promedio(numero1, numero2, numero3):
    return (numero1 + numero2 + numero3) / 3


# Ejercicio 8: Un banco necesita para sus cajeros automáticos un programa que lea una cantidad
# de dinero e imprima a cuántos billetes equivale, considerando que existen billetes
# de $100, $50, $10, $5 y $1. Desarrollar dicho programa de tal forma que se
# minimice la cantidad de billetes entregados por el cajero.

def cantDinero(dinero):
    return {
        "$100": dinero / 100,
        "$50": dinero / 50,
        "$10": dinero / 10,
        "$5": dinero / 5,
        "$1": dinero
    }


# Ejercicio 9: Una inmobiliaria paga a sus vendedores un salario de $800, más una comisión de
# $50 por cada venta realizada, más el 5% del valor de esas ventas. Realizar un
# programa que imprima el número del vendedor y el salario que le corresponde en
# un determinado mes. Se leen el número del vendedor, la cantidad de ventas que
# realizó y el valor total de las mismas.

def calcularSalario(idVendedor, ventas):
    salario = 800
    porcentajePorVenta = 5
    comisionPorVenta = 50

    acumularGananciasventas = 0
    for venta in ventas:
        acumularGananciasventas = acumularGananciasventas + (porcentajePorVenta * venta) / 100

    return {
        "idVendedor": idVendedor,
        "salario": salario + (len(ventas) * comisionPorVenta) + acumularGananciasventas
    }


# Ejercicio 10: Leer un período en segundos e imprimirlo expresado en días, horas, minutos y
# segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y
# 20 segundos.

def segundosTofullTime(segundos):
    str(datetime.timedelta(segundos))


# Ejercicio 11: Desarrollar un programa que solicite una temperatura expresada en grados
# centígrados y la imprima convertida a grados Fahrenheit, tal que:

def centigradosToFahrenheit(centigrados):
    return (centigrados * (9 / 5)) + 32

# Ejercicio 12: Escribir un programa para convertir un número binario de 4 cifras en un número
# decimal.

# ingreso "1001" -> 2 al cubo + 2 a la 0

# 1001 % 10 = 1 var1
# 1001 // 10 = 100 % 10 = 0 var 2
# 100 // 10 = 10 % 10 = 0 var 3
# 10//10 = 1 var 4

# 2 elevado a la 3  * var 4 + 2 elevado a la 2 * var 3 .....
