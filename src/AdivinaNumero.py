import random

def comparar_numeros(num_aleatorio, numero_input):
    """
    Compara dos numeros
    :param num_aleatorio: numero a adivinar
    :param numero_input: numero introducido por el jugador
    :return: devuelve verdadero si ambos son iguales sino false
    """
    if numero_input==num_aleatorio:
        return True
    else:
        return False

def mayor_menor(num_aleatorio, numero_input):
    if numero_input>num_aleatorio:
        return "mayor"
    else:
        return "menor"
intentos = 3
hechos = 0
segundo_numero_inter = 10
numero_aleatorio = round(random.uniform(0,segundo_numero_inter),1)
print("Este es un juego de adivinar numeros del 0 al 10, tiene un total de " + str(intentos) + " intentos")
while hechos<intentos:
    numero = float(input("Introduzca un numero:"))
    if comparar_numeros(numero_aleatorio, numero):
        print("Has ganado en un total de " + str(hechos+1) + " intentos")
        break
    elif numero>segundo_numero_inter:
        print("Has introducido un numero no valido por favor vuelve a introducir")
        continue
    else:
        hechos += 1
        print("Intentalo otra vez el numero que has introducido es " + mayor_menor(numero_aleatorio, numero) + "\nTe quedan " + str(intentos-hechos) + " intentos")
        if hechos==intentos:
            print("Se han acabado los intentos")
            print("El numero era: " + str(numero_aleatorio))
