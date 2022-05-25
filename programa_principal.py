#-------------------------------------------------------------------------------------
import mostrar_numeros_impares_cantidad

import mostrar_numeros_pares_cantidad

import mostrar_numeros_perfectos_rango

import mostrar_numeros_perfectos_cantidad

import maximo_comun_divisor_dos_numeros

#-------------------------------------------------------------------------------------
def menu():
    print("Estas son las opciones matemáticas que hay")
    
    print("\n2.- Mostrar números impares en un rango\n")
    print("\n3.- Mostrar números pares en un rango\n")
    print("\n4.- Mostrar los números perfectos en un rango\n")
    print("\n5.- Mostrar una cantidad de números perfectos desde el 1\n")
    print("\n6.- Realizar el Máximo Común Divisor de dos números\n")

#-------------------------------------------------------------------------------------
#Programa principal
def programa_principal():
    opcn_usuario = int(input("Introduzca la opción que desea utilizar\n"))
    if opcn_usuario == 1:
        print()
    elif opcn_usuario == 2:
        print("\nHa elegido mostrar numeros impares y la cantidad entre ellos\n")
        mostrar_numeros_impares_cantidad.numeros_impares_cantidad()
    elif opcn_usuario == 3:
        print("\nHa elegido mostrar numeros pares y la cantidad entre ellos\n")
        mostrar_numeros_pares_cantidad.numeros_pares_cantidad()
    elif opcn_usuario == 4:
        print("\nHa elegido mostrar los numeros perfectos en un rango\n")
        mostrar_numeros_perfectos_rango.numeros_perfectos_rango()
    elif opcn_usuario == 5:
        print("\nHa elegido mostrar la cantidad de numeros perfectos empezando desde 1\n")
        mostrar_numeros_perfectos_cantidad.numeros_perfectos_cantidad()
    elif opcn_usuario == 6:
        print("\nHa elegido el Máximo Común Divisor de dos números\n")
        maximo_comun_divisor_dos_numeros.mcd_dos_numeros()


#-------------------------------------------------------------------------------------
#Ejecución de la función del programa principal
if __name__ == "__main__":
    programa_principal()
