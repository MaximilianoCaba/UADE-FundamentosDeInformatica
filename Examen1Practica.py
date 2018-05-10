"""
leer dos numeros enteros A y B, verifique que A sea menor o igual que B.
intercambiar los valores en caso de no cumplirse esta condicion.
Luego se solicita imprimir por pantalla los multiplos de 5 comprendidos entre A y B
"""


def leerNumero():
    return int(input("ingrese un numero"))


def multiplos_de_cinco():
    numero_a = leerNumero()
    numero_b = leerNumero()

    if (numero_a > numero_b):
        variable_temporal = numero_a
        numero_a = numero_b
        numero_b = variable_temporal

    for i in range(numero_a, numero_b + 1):
        if (i % 5) == 0:
            print("el numero ", i, "es multiplo de 5")


# multiplos_de_cinco()

"""
Leer 3 numeros enteros, asegurandose que ninguno este repetido, si se ingresa un valor repetido
se lo rechaza con un mensaje de error y se volvera a solicitar el numero.
Una vez ingresadolos 3 numeros se solicita descartar el que posee valor intermedio y mostrar el 
promedio de los otros dos numeros
"""


def leerNumeroCondicionado(numero_1, numero_2):
    while True:
        numero_input = leerNumero()
        if numero_1 != numero_2 and numero_2 != numero_input and numero_1 != numero_input:
            return numero_input
        else:
            print("ingrese otro numero")


def esMayor(numero_posicion, numero):
    if numero > numero_posicion:
        return numero
    else:
        return numero_posicion


def esMenor(numero_menor, numero):
    if numero < numero_menor:
        return numero
    else:
        return numero_menor


def obtenerMayorMenor(numero_1, numero_2, numero_3):
    numero_mayor = 0
    numero_menor = 99999999

    numero_mayor = esMayor(numero_mayor, numero_1)
    numero_mayor = esMayor(numero_mayor, numero_2)
    numero_mayor = esMayor(numero_mayor, numero_3)

    numero_menor = esMenor(numero_menor, numero_1)
    numero_menor = esMenor(numero_menor, numero_2)
    numero_menor = esMenor(numero_menor, numero_3)

    return numero_mayor, numero_menor


numero_1 = leerNumeroCondicionado("NULL_1", "NULL_2")
numero_2 = leerNumeroCondicionado(numero_1, "NULL_3")
numero_3 = leerNumeroCondicionado(numero_1, numero_2)

numero_mayor, numero_menor = obtenerMayorMenor(numero_1, numero_2, numero_3)

print((numero_mayor + numero_menor) / 2)
