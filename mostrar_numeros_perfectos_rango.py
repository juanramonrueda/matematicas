def funcion_principal():
    #-------------------------------------------------------------------------------------------------------------------------------
    contador_perfectos = 0

    #-------------------------------------------------------------------------------------------------------------------------------
    primer_numero = int(input("\nIntroduzca el primer número\n"))

    segundo_numero = int(input("\nIntroduzca el segundo número\n"))

    #-------------------------------------------------------------------------------------------------------------------------------
    #Intercambio de variables para realizar el FOR correctamente
    if primer_numero > segundo_numero:
        aux = primer_numero
        primer_numero = segundo_numero
        segundo_numero = aux

    #-------------------------------------------------------------------------------------------------------------------------------
    #Con el primer FOR recorro desde el primer número hasta el segundo número, actuando como el dividendo
    for dividendo in range(primer_numero, segundo_numero):
        #Inicializo la variable a 0 dentro del bucle para que cuando entre a un número se reinicie y haga su función
        suma_divisores = 0
        
        #Con el segundo FOR recorro desde el número 1 hasta el número máximo - 1 que haya en el primer FOR, actuando como divisor
        for divisor in range(1, dividendo):
            #Si el módulo de la división es 0, entonces hago la suma de los divisores
            if dividendo % divisor == 0:
                suma_divisores = suma_divisores + divisor
        
        #Si la suma de los divisores es igual al número que hay en el primer FOR, entonces es un número perfecto
        if dividendo == suma_divisores:
            contador_perfectos = contador_perfectos + 1
            print(f'\nEl número {dividendo} es un número perfecto\n')
    
    #-------------------------------------------------------------------------------------------------------------------------------
    if contador_perfectos == 0:
        print(f'\nNo hay números perfectos entre el número {primer_numero} y el número{segundo_numero}\n')
    
    elif contador_perfectos == 1:
        print(f'\nEntre el número {primer_numero} y el número {segundo_numero} hay {contador_perfectos} número\n')
    
    else:
        print(f'\nEntre el número {primer_numero} y el número {segundo_numero} hay {contador_perfectos} números\n')