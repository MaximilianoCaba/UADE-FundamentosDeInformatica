"""
cargar una lista con 6 valores,
realizar la suma de los valores que estan en posiciones impares

cont = 0
list = []

while cont < 6:
    list.append(int(input("ingrese un valor")))
    cont += 1

cont = 1
suma = 0
while cont < 6:
    suma = suma + list[cont]
    cont += 2

print(suma)

"""
"""
# cargar una lista de 6 valores, sumar los valores que estan en ubicaciones pares
# y multiplicar los valores de posiciones impares

list = []
sum = 0
multi = 1
for i in range(6):
    list.append(int(input("ingrese un valor")))

for i in range(6):
    if (i % 2) == 0:
        sum += list[i]
    else:
        multi *= list[i]

print(sum)
print(multi)
"""

## BURBUJEO
"""
a = [9, 9, 3, 2, 1]

for j in range(len(a) - 1):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
print(a)
"""

## BURBUJEO turbo

"""
a = [9, 8, 3, 2, 1]

bandera = True

while bandera:
    bandera = False
    for i in range(len(a) - 1):

        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            bandera = True

print(a)
"""

## metodo de seleccion

"""
a = [9, 7, 5, 3, 1, 6]

for j in range(len(a) - 1):
    for i in range(j + 1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
"""

"""
ingresar dos valores A y B menores a 1000, obtener su producto utilizando el metodo egipcio
"""

"""
def ingresarValor(valueName):
    a = 1001
    while a > 1000:
        a = int(input("ingrese un numero " + valueName))
    return a


def generarListas(numero_a, numero_b):
    list_a = []
    list_b = []
    count = 0
    raiz_dos = 2 ** count

    while raiz_dos <= numero_a:
        list_a.append(raiz_dos)
        list_b.append(raiz_dos * numero_b)
        count += 1
        raiz_dos = 2 ** count

    return list_a, list_b


def calcularNumeroEgipcio(list_a, list_b, numero_a):
    resultado_a = 0
    resultado_b = 0
    count = len(list_a) - 1
    for i in list_a[::-1]:
        aux = resultado_a + i
        if aux <= numero_a:
            resultado_a = aux
            resultado_b = resultado_b + list_b[count]
        count -= 1
    return resultado_b


numero_a = ingresarValor("A")
numero_b = ingresarValor("B")
list_a, list_b = generarListas(numero_a, numero_b)
resultado = calcularNumeroEgipcio(list_a, list_b, numero_a)
print(resultado)
"""



## buscar:
## ordenamiento secuencial
"""
lista = [4, 3, 8, 7]
posicion = -1
contador = 0
bandera = 0
valor = 8

while contador < len(lista) and bandera == 0:
    if lista[contador] == valor:
        bandera = 1
        posicion = contador
    else:
        contador += 1

if bandera == 1:
    print(posicion)
else:
    print("no esta en la lista")
"""

## ordenamiento binario
"""
lista = [4, 3, 8, 7]
posicion = -1
valor = 8
min = 0
max = len(lista) - 1

while min <= max and posicion == -1:
    medio = (min + max) // 2
    if valor == len(medio):
        posicion = medio
    if valor > lista[medio]:
        min = medio + 1
    else:
        max = medio - 1

if posicion != -1:
    print(posicion)
else:
    print("El valor no esta en la lista")
     
"""

