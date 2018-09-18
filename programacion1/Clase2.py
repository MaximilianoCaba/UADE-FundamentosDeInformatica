def calcular_viaje(cantidad_viajes):
    """
    calcula los viajes de una persona
    dependiendo la cantidad se aplica un valor
    """

    valor_total = 0

    for i in range(1, cantidad_viajes + 1):

        if i <= 20:
            valor_total += 12.5

        if 21 < i <= 30:
            valor_total += 10

        if 31 < i <= 40:
            valor_total += 8.75

        if 41 < i <= 45:
            valor_total += 7.5

    return valor_total


def ingresar_valor_menor_45():
    texto_a_mostrar = "ingresar un numero menor a 46 positivo"
    numero = int(input(texto_a_mostrar))
    while numero < 0 or numero > 45:
        numero = int(input(texto_a_mostrar))
    return numero


cant_viaje = ingresar_valor_menor_45()
print("el valor de", cant_viaje, "viajes es", calcular_viaje(cant_viaje))
