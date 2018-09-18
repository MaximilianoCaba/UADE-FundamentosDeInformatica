import random


def buildMatriz(list, rows, colums):
    for i in range(rows):
        list.append([0] * colums)


def generateRandomNumber():
    number = random.randint(0, 999)
    return number * number


def chargeMatriz(list):
    list_number_uniq = []

    for (i, value) in enumerate(list):
        for (j, value2) in enumerate(value):
            number = generateRandomNumber()
            while number in list_number_uniq:
                number = generateRandomNumber()
            list_number_uniq.append(number)

            list[i][j] = number


def printMatriz(list):
    for (i, value) in enumerate(list):
        for (j, value2) in enumerate(value):
            print("%3d" %list[i][j], end="")
        print()


list = []
buildMatriz(list, 4, 4)
chargeMatriz(list)
printMatriz(list)
