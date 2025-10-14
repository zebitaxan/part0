"""
Módulo para asignación de pesos a competencias.
"""
from .embedding_matcher import obtener_similitud

def asignar_pesos(keywords, prioridades, base_competencias):
    perfil = {}
    for skill in base_competencias:
        similitud = obtener_similitud(keywords, skill["keywords"])
        peso_base = similitud
        if skill["nombre"] in prioridades:
            peso_base += 0.2
        perfil[skill["nombre"]] = round(min(peso_base, 1.0), 2)
    return perfil
