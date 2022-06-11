def funcion_principal():
    #----------------------------------------------------------------------------------------------------
    primer_rango = int(input("\nIntroduzca el primer rango\n"))

    segundo_rango = int(input("\nIntroduzca el segundo rango\n"))

    #----------------------------------------------------------------------------------------------------
    cantidad = 0

    imprimir = str

    #----------------------------------------------------------------------------------------------------
    if segundo_rango < primer_rango:
        aux = segundo_rango
        segundo_rango = primer_rango
        primer_rango = aux

    #----------------------------------------------------------------------------------------------------
    for dividendo in range(primer_rango, segundo_rango):
        if dividendo % 2 == 0:
            print(dividendo)
            cantidad = cantidad + 1

    #----------------------------------------------------------------------------------------------------
    imprimir = str(input("¿Quiere conocer la cantidad de números pares?\n"))
    
    if imprimir == "s":
        print(f'\nLa cantidad de números pares entre {primer_rango} y {segundo_rango} es: {cantidad}\n')