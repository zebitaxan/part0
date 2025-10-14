"""
Funciones auxiliares para procesamiento de texto.
"""
def normalizar_lista(lista):
    return [x.lower().strip() for x in lista]
