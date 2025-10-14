"""
Entrada principal del sistema de generación de perfiles laborales por IA.
"""
from analyzer.text_cleaner import limpiar_texto
from analyzer.keyword_extractor import extraer_keywords
from analyzer.embedding_matcher import obtener_similitud
from analyzer.weight_assigner import asignar_pesos
import json

# Cargar base de competencias
with open("src/data/skills_base.json", "r", encoding="utf-8") as f:
    base_competencias = json.load(f)

def generar_perfil_puesto(respuestas, base_competencias):
    texto = limpiar_texto(respuestas["descripcion"])
    keywords = extraer_keywords(texto)
    prioridades = respuestas.get("prioridades", [])
    perfil = asignar_pesos(keywords, prioridades, base_competencias)
    return perfil

if __name__ == "__main__":
    # Ejemplo de entrada
    respuestas = {
        "descripcion": "Buscamos un comercial B2B con buena comunicación, persistente y enfocado en resultados.",
        "prioridades": ["Cierre de ventas", "Comunicación", "Resiliencia"]
    }
    perfil = generar_perfil_puesto(respuestas, base_competencias)
    print(json.dumps(perfil, ensure_ascii=False, indent=2))
