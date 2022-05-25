def mcd_dos_numeros():
    #------------------------------------------------------------------------------------------------------------------------------------
    resultado = -1 #Inicializo la variable a un número distinto de 0 para que entre al bucle

    #------------------------------------------------------------------------------------------------------------------------------------
    primer_numero = int(input("\nIntroduzca el primer número\n"))
    primer_numero_calculos = primer_numero #Hago que se guarde en otra variable para realizar operaciones con ella

    segundo_numero = int (input("\nIntroduzca el segundo número\n"))
    segundo_numero_calculos = segundo_numero #Hago que se guarde en otra variable para realizar operaciones con ella
    
    #------------------------------------------------------------------------------------------------------------------------------------
    #Esta función es para que se realice correctamente las restas posteriores y que no salgan números negativos
    def intercambiar_variables(primer_numero_calculos, segundo_numero_calculos):
        aux = segundo_numero_calculos
        segundo_numero_calculos = primer_numero_calculos
        primer_numero_calculos = aux

        return primer_numero_calculos, segundo_numero_calculos

    #------------------------------------------------------------------------------------------------------------------------------------
    if primer_numero_calculos < segundo_numero_calculos:
            primer_numero_calculos, segundo_numero_calculos = intercambiar_variables(primer_numero_calculos, segundo_numero_calculos)

    #------------------------------------------------------------------------------------------------------------------------------------
    #El cálculo del Máximo Común Divisor se realiza mediante restas sucesivas hasta que el resultado de las restas sea 0
    while resultado != 0:

        resultado = primer_numero_calculos - segundo_numero_calculos #Guardo el resultado de la resta
        
        cambio = 0
        #Intercambio las variables para poder realizar el MCD ya que el segundo número debe almacenarse en la primera variable y 
        # que el resultado se almacene en la segunda variable para continuar con el MCD
        if cambio == 0: 
            primer_numero_calculos = segundo_numero_calculos
            segundo_numero_calculos = resultado
        
        if primer_numero_calculos < segundo_numero_calculos:
            primer_numero_calculos, segundo_numero_calculos = intercambiar_variables(primer_numero_calculos, segundo_numero_calculos)

        if primer_numero_calculos == segundo_numero_calculos:
            print(f'\nEl máximo común divisor de los números {primer_numero} y {segundo_numero} es {primer_numero_calculos}')