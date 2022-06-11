#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
import time

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def funcion_principal():
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    input("\nSi intenta mostrar la cantidad de números perfectos superior a 4 puede parecer que está pillado, está realizando operaciones\n")
    #Hago una pequeña pausa antes de pedir la cantidad de números perfectos que quiere ver
    time.sleep(2)

    cantidad_total_mostrar = int(input("\nIntroduzca la cantidad de números perfectos que quiere ver empezando desde el número 1\n"))

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    cantidad_numeros_perfectos = 0

    dividendo = 0

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    while cantidad_numeros_perfectos < cantidad_total_mostrar:
        dividendo = dividendo + 1
        suma_divisores = 0
        
        for divisor in range(1, dividendo):
            if dividendo % divisor == 0:
                suma_divisores = suma_divisores + divisor
        
        if dividendo == suma_divisores:
            print(f'\nEl número {dividendo} es un número perfecto\n')
            cantidad_numeros_perfectos = cantidad_numeros_perfectos + 1