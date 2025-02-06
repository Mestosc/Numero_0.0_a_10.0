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
    """
    Compara si el numero que el usuario introduce es mayor al numero aleatorio ya disponible
    :param num_aleatorio: el numero aleatorio proporcionado por el programa
    :param numero_input: el numero del usuario que pasamos por aqui
    :return: si numero_input es mayor a numero_aleatorio devuelve mayor en caso contrario menor
    """
    if numero_input>num_aleatorio:
        return "mayor"
    else:
        return "menor"
intentos = 4 # Numero de intentos
hechos = 0
segundo_numero_inter = 10 # El numero hasta el que queremos saber
numero_aleatorio = round(random.uniform(0,segundo_numero_inter),1)
print("Este es un juego de adivinar numeros del 0 al 10, tiene un total de " + str(intentos) + " intentos")
while hechos<intentos:
    numero = float(input("Introduzca un numero:"))
    if numero>segundo_numero_inter:
        print("Has introducido un numero no valido por favor vuelve a introducir")
        continue
    elif comparar_numeros(numero_aleatorio, numero):
        print("Has ganado en un total de " + str(hechos+1) + " intentos")
        break
    else:
        hechos += 1
        print("Intentalo otra vez el numero que has introducido es " + mayor_menor(numero_aleatorio, numero) + "\nTe quedan " + str(intentos-hechos) + " intentos")
        if hechos==intentos:
            print("Se han acabado los intentos")
            print("El numero era: " + str(numero_aleatorio))
