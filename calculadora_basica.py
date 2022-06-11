#-----------------------------------------------------------------------------------------------------------------
#Importación de los módulos esenciales para esta parte
import limpiar_pantalla

import math

import time

#-----------------------------------------------------------------------------------------------------------------
#Muestra un menú con las opciones disponibles
def menu():
    limpiar_pantalla.limpiar_sin_preguntar()
    print("\n1.- Suma de dos números\n")
    print("\n2.- Resta de dos números\n")
    print("\n3.- Multiplicación de dos números\n")
    print("\n4.- División (cociente) de dos números\n")
    print("\n5.- División (resto) de dos números\n")
    print("\n6.- Potencias\n")
    print("\n7.- Calculo de raices\n")
    print("\n8.- Realizar el sumarial de un número\n")
    print("\n9.- Realizar el factorial de un número\n")
    print("\n10.- Salir de Calculadora\n")

#-----------------------------------------------------------------------------------------------------------------
#Programa principal de calculadora_basica
def calculadora():
    #-------------------------------------------------------------------------------------------------------------
    #Inicialización de variable para entrar al bucle
    opcn_usuario = 1

    #-------------------------------------------------------------------------------------------------------------
    while opcn_usuario != 10:
        menu()
        
        opcn_usuario = int(input("\nEscoga la opción que desee usar\n"))
        
        if opcn_usuario == 1:
            numero_1, numero_2, suma = sumar()
            print(f"\nEl resultado de sumar los números {numero_1} y {numero_2} es {suma}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
        
        elif opcn_usuario == 2:
            numero_1, numero_2, resta = restar()
            print(f"\nEl resultado de restar los números {numero_1} y {numero_2} es {resta}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
        
        elif opcn_usuario == 3:
            numero_1, numero_2, multiplicacion = multiplicar()
            print(f"\nEl resultado de multiplicar los números {numero_1} y {numero_2} es {multiplicacion}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
        
        elif opcn_usuario == 4:
            numero_1, numero_2, cociente = dividir_cociente()
            print(f"\nEl cociente de dividir el número {numero_1} entre {numero_2} es {cociente}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
        
        elif opcn_usuario == 5:
            numero_1, numero_2, resto = dividir_resto()
            print(f"\nEl resto de dividir el número {numero_1} entre {numero_2} es {resto}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
        elif opcn_usuario == 6:
            base, exponente, potencia_resultante = potencias()
            print(f"\nLa potencia de la base {base} elevada a {exponente} es {potencia_resultante}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
        
        elif opcn_usuario == 7:
            radicando, indice, raiz_resultante = raices()
            print(f"\nLa raíz del radicando {radicando} con índice {indice} es {raiz_resultante}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")

        elif opcn_usuario == 8:
            numero, suma_numero = sumarial()
            print(f"\nEl resultado del sumarial del número {numero} es {suma_numero}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
        
        elif opcn_usuario == 9:
            numero, factorial_numero = factorial()
            print(f"\nEl resultado del factorial del número {numero} es {factorial_numero}\n")
            time.sleep(2)
            input("\nPulse la tecla Intro o Enter para continuar...")
    
#-----------------------------------------------------------------------------------------------------------------
def sumar():
    numero_1 = float(input("\nIntroduzca el primer número\n"))

    numero_2 = float(input("\nIntroduzca el segundo número\n"))

    suma_numeros = numero_1 + numero_2

    return numero_1, numero_2, suma_numeros

#-----------------------------------------------------------------------------------------------------------------
def restar():
    numero_1 = float(input("\nIntroduzca el primer número\n"))

    numero_2 = float(input("\nIntroduzca el segundo número\n"))

    resta_numeros = numero_1 - numero_2

    return numero_1, numero_2, resta_numeros

#-----------------------------------------------------------------------------------------------------------------
def multiplicar():
    numero_1 = float(input("\nIntroduzca el primer número\n"))

    numero_2 = float(input("\nIntroduzca el segundo número\n"))

    multiplicacion_numeros = numero_1 * numero_2

    return numero_1, numero_2, multiplicacion_numeros

#-----------------------------------------------------------------------------------------------------------------
def dividir_cociente():
    numero_1 = float(input("\nIntroduzca el dividendo\n"))

    numero_2 = float(input("\nIntroduzca el divisor\n"))

    cociente_numeros = numero_1 / numero_2

    return numero_1, numero_2, cociente_numeros

#-----------------------------------------------------------------------------------------------------------------
def dividir_resto():
    numero_1 = float(input("\nIntroduzca el dividendo\n"))

    numero_2 = float(input("\nIntroduzca el divisor\n"))

    resto_numeros = numero_1 % numero_2

    return numero_1, numero_2, resto_numeros

#-----------------------------------------------------------------------------------------------------------------
def potencias():
    base = float(input("\nIntroduzca la base\n"))

    exponente = int(input("\nIntroduzca el exponente\n"))

    potencia = math.pow(base, exponente)

    return base, exponente, potencia

#-----------------------------------------------------------------------------------------------------------------
def raices():
    radicando = float(input("\nIntroduzca el radicando o base de la raíz\n"))

    while radicando < 0:
        radicando = float(input("\nIntroduzca un radicando o base mayor o igual a 0\n"))

    indice = int(input("\nIntroduzca el índice de la raíz\n"))

    while indice <= 1:
        indice = int(input("\nIntroduzca un índice mayor o igual que 2\n"))

    #Mediante la función pow se pueden realizar raices con distintos índices
    raiz = pow(radicando, 1/indice)
    
    return radicando, indice, raiz

#-----------------------------------------------------------------------------------------------------------------
def sumarial():
    #-------------------------------------------------------------------------------------------------------------
    suma_numero = 0

    #-------------------------------------------------------------------------------------------------------------
    numero = int(input("\nIntroduzca el número (positivo) para realizar el sumarial\n"))

    #-------------------------------------------------------------------------------------------------------------
    #Comprobación que el número es mayor que 0
    while numero < 0:
        numero = int(input("\nIntroduzca un número mayor o igual que 0\n"))
    
    #-------------------------------------------------------------------------------------------------------------
    #Cálculo del sumarial del número introducido
    for numeros in range(1, numero + 1):
        suma_numero = suma_numero + numeros

    return numero, suma_numero

#-----------------------------------------------------------------------------------------------------------------
def factorial():
    #-------------------------------------------------------------------------------------------------------------
    #Se inicializa esta variable a 1 para que los factoriales de 0! y 1! tengan resultado 1
    factorial_numero = 1

    #-------------------------------------------------------------------------------------------------------------
    numero = int(input("\nIntroduzca el número (positivo) para realizar el factorial\n"))

    while numero < 0:
        numero = int(input("\nIntroduzca un número mayor o igual que 0\n"))
    
    for numeros in range(numero, 0, -1):
        factorial_numero = factorial_numero * numeros
    
    return numero, factorial_numero