#-------------------------------------------------------------------------------------
#Importación de módulos propios para el funcionamiento del programa
import calculadora_basica

import mostrar_numeros_impares_cantidad

import mostrar_numeros_pares_cantidad

import mostrar_numeros_perfectos_rango

import mostrar_numeros_perfectos_cantidad

import maximo_comun_divisor_dos_numeros

import ecuacion_segundo_grado

import limpiar_pantalla

#-------------------------------------------------------------------------------------
def menu():
    print("Estas son las opciones matemáticas que hay")
    print("\n1.- Calculadora básica\n")
    print("\n2.- Mostrar números impares en un rango\n")
    print("\n3.- Mostrar números pares en un rango\n")
    print("\n4.- Mostrar los números perfectos en un rango\n")
    print("\n5.- Mostrar una cantidad de números perfectos desde el 1\n")
    print("\n6.- Realizar el Máximo Común Divisor de dos números\n")
    print("\n10.- Realizar ecuaciones de segundo grado\n")
    print("\n11.- Salir\n")

#-------------------------------------------------------------------------------------
#Programa principal
def main():

    opcn_usuario = 1

    while opcn_usuario != 11:
        limpiar_pantalla.limpiar_preguntando()
        menu()

        opcn_usuario = int(input("\nIntroduzca la opción que desea utilizar\n"))
    
        if opcn_usuario == 1:
            calculadora_basica.funcion_principal()
        
        elif opcn_usuario == 2:
            print("\nHa elegido mostrar numeros impares y la cantidad entre ellos\n")
            mostrar_numeros_impares_cantidad.funcion_principal()
        
        elif opcn_usuario == 3:
            print("\nHa elegido mostrar numeros pares y la cantidad entre ellos\n")
            mostrar_numeros_pares_cantidad.funcion_principal()
        
        elif opcn_usuario == 4:
            print("\nHa elegido mostrar los numeros perfectos en un rango\n")
            mostrar_numeros_perfectos_rango.funcion_principal()
        
        elif opcn_usuario == 5:
            print("\nHa elegido mostrar la cantidad de numeros perfectos empezando desde 1\n")
            mostrar_numeros_perfectos_cantidad.funcion_principal()
        
        elif opcn_usuario == 6:
            print("\nHa elegido el Máximo Común Divisor de dos números\n")
            maximo_comun_divisor_dos_numeros.funcion_principal()

        elif opcn_usuario == 10:
            print("Ha elegido realizar operaciones con ecuaciones de segundo grado\n")
            ecuacion_segundo_grado.funcion_principal()


#-------------------------------------------------------------------------------------
#Ejecución de la función del programa principal
if __name__ == "__main__":
    main()