import os
#---------------------------------------------------------------------------
#Principalmente es para Linux y sistemas operativos basados en MS-DOS
def limpiar_sin_preguntar():
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)

#---------------------------------------------------------------------------
def limpiar_preguntando():
    limpiar_pantalla = str(input("\n¿Quiere limpiar la pantalla\n"))
    if limpiar_pantalla == "s":
        comando = 'clear'
        if os.name in ('nt', 'dos'):
            comando = 'cls'
        os.system(comando)