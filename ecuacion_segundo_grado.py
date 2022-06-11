#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math

import time

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def funcion_principal():
    informacion()

    valor_a , valor_b, valor_c = preguntar_valores()

    variable_a, variable_b, variable_c, resultados_ecuacion = realizar_ecuacion(valor_a, valor_b, valor_c)

    print(f"Los resultados de la ecuación {variable_a}x² + {variable_b}x - {variable_c} = 0; son {resultados_ecuacion}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def informacion():
    print("Este programa usa con el formato ax² + bx - c = 0; para realizar la inversión de la operación use el símbolo más '+' o el símbolo menos '-' según la situación")
    time.sleep(2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def preguntar_valores():
    valor_a = int(input("\nIntroduzca el valor de la letra a\n"))
    valor_b = int(input("\nIntroduzca el valor de la letra b\n"))
    valor_c = int(input("\nIntroduzca el valor de la letra c\n"))

    return valor_a, valor_b, valor_c

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def realizar_ecuacion(valor_a, valor_b, valor_c):
    if valor_a == 0:
        if valor_b == 0:
            resultado = "La ecuación no tiene solución"
        
        else:
            resultado = (-valor_c / valor_b)
    
    elif valor_a != 0:
        discriminante = (math.pow(valor_b, 2) - (4 * valor_a * valor_c))

        if discriminante < 0:
            resultado = "La ecuación no tiene solución real"
        
        else:
            resultado_raiz = math.sqrt(discriminante)
            primera_solucion = ((-valor_b + resultado_raiz) / (2 * valor_a))
            segunda_solucion = ((-valor_b - resultado_raiz) / (2 * valor_a))
            resultado = primera_solucion, segunda_solucion
    
    return valor_a, valor_b, valor_c, resultado
