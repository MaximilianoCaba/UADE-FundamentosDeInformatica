def aniobisiesto(yyyy):
    if yyyy % 4 == 0:
        if yyyy % 100 == 0:
            if yyyy % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def diasiguiente(dd, mm, yyyy):
    diasFebrero = 29

    if aniobisiesto(yyyy):
        diasFebrero = 28

    lista = [31, diasFebrero, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]

    if lista[mm - 1] == dd and mm == 12:
        return 1, 1, yyyy + 1

    if lista[mm - 1] == dd and mm != 12:
        return 1, mm + 1, yyyy

    if lista[mm - 1] != dd:
        return dd + 1, mm, yyyy


def aumentarDias(dia, mes, anio, cantidad_dias):
    for n in range(0, cantidad_dias):
        dia, mes, anio = diasiguiente(dia, mes, anio)

    return dia, mes, anio


def cantidadDiasEntreFechas(diaA, mesA, anioA, diaB, mesB, anioB):
    cont = 0
    flag = True

    while flag:
        (diaA, mesA, anioA) = diasiguiente(diaA, mesA, anioA)
        cont += 1
        if (diaA, mesA, anioA) == (diaB, mesB, anioB):
            flag = False

    return cont


# divisible por 4 y no por 100 / divisible por 4, por 100 y por 400


print(diasiguiente(31, 12, 2018))

print(diasiguiente(30, 11, 2018))

print(diasiguiente(25, 12, 2018))

print(diasiguiente(28, 2, 2016))

dia = 1
mes = 1
anio = 2018
cantidad_dias_sumar = 20

print(aumentarDias(dia, mes, anio, cantidad_dias_sumar))

print(cantidadDiasEntreFechas(1, 1, 2018, 1, 1, 2019))


## matriz espiral

"""
1.1 -> 1.2 -> 1.3 -> 1.4

2.4 -> 3.4 -> 4.4

4.3 -> 4.2 -> 4.1

3.1 -> 2.1

2.2 -> 2.3

3.3 -> 3.2

"""


# Python3 program to print
# given matrix in spiral form
def spiralPrint(m, n, a):
    k = 0;
    l = 0

    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''

    while (k < m and l < n):

        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
        print()

        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        print()
        n -= 1

        # Print the last row from
        # the remaining rows
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")

            m -= 1
        print()
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")

            l += 1
        print()

# Driver Code
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

R = 3;
C = 6
spiralPrint(R, C, a)