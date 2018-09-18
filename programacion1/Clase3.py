# Metodos Lista
# insert(i,n)
# pop(i)
# append(n)
# remove(n)
# index(n) / index(inicio, numero / fin)
# count(n)
# clear()
# reverse()
# sort() / sort(reverse=True)


# Funciones Random
# import random
# random.random() -> [0,1)
# random.randint(min, max)
# random.choise(string)
# random.seed(numero) -> mantiene secuencia de repeticion de pruebas


# ejercicio9

# [1,1,2] -> [0.25,0.25,0.5]
"""
def normalizarLista(lista):
    listaNormalizada = []
    for i in lista:
        listaNormalizada.append(lista[i] / sum(lista))
    return listaNormalizada


print(normalizarLista([1, 1, 2]))
"""

# ejercicio1
import random


# cargar un vector random de dos digitos con numeros al azar con 4 digitos


def cargarVector():
    lista = []
    for i in range(0, random.randint(10, 99)):
        lista.append(random.randint(1000, 9999))
    return lista


# devolver la suma de la lista anterior
print(sum(cargarVector()))


# eliminar todos los valores repetidos de la lista, se recibe como parametro

def eliminarRepetidos(lista, valor):
    lista.sort()

    if lista.count(valor) > 2:
        posicion = lista.index(valor)

        while posicion != -1:
            if lista[posicion + 1] == valor:
                lista.pop(posicion + 1)
            else:
                posicion = -1
    return lista


print(eliminarRepetidos([1, 1, 1, 2], 1))


def lista_capicua(lista):
    isCapicua = True
    for i in lista:
        if lista[i] != lista.reverse()[i]:
            isCapicua = False

    return isCapicua


print(lista_capicua([1, 2, 1]))

lista = []
