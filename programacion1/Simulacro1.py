"""
Simulacro 1 (no se permite el uso de elementos no tratados en clase)

1 - Escriba un programa que utilice una funcion para devolver la suma de los
    primeros digitos  de cada numero almacenado en una lista de enteros.
    Los valores se ingresan a traves del teclado, finalizando la carga con -1.
    Los numeros de la lista pueden ser positivos o negrativos, pero el digito a
    sumar siempre sera positivo. Imprimir la lista y la suma obtenida

Ejemplo -> [22, -15, 7, 456] -> 2 + 1 + 7 + 4 = 14


2 - Desarrollar un programa para ingresar un numero entero N, impar y no menos que 3.
    Rechazar el numero y volverlo a ingresar en caso de no satisfacer estas condiciones.
    Luego se solicita imprimir el borde de un triangulo centrado de N filas, tal como se muestra
    a continuacion

Ejemplo -> N = 5

            *
           * *
          *   *
         *     *
        * * * * *
"""

"""
## ejercicio 1
def sum_first_number_for_list(list_number):
    result = 0
    for number in list_number:

        number = str(number)
        if number[0] == "-":
            number = number[1]
        else:
            number = number[0]
        result += int(number)

    return result

numero = 0
list_number = []
while numero != -1:
    numero = int(input("Ingrese un numero, para finalizar ingrese -1"))
    if numero != -1:
        list_number.append(numero)

print(sum_first_number_for_list(list_number))
print(list_number)
"""

"""
#Ejercicio 2
def input_valid_number():
    flag = True
    numero = 0
    while flag:
        numero = int(input("ingrese un N entero, N > 3, N = impar"))

        if numero > 3 and (numero % 2) != 0:
            flag = False

    return numero


def print_pyramid(rows):
    for i in range(rows):
        if i == 0 or i == (rows - 1):
            print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
        elif i != 0 and i != (rows - 1):
            print(' ' * (rows - i - 1) + '*' + ' ' * (2 * i - 1) + '*')


print_pyramid(input_valid_number())
"""