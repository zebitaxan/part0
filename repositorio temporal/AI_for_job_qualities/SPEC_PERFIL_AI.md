# Talent Match AI System — Documentación Técnica

## Descripción general
Este sistema genera perfiles laborales ideales a partir de respuestas empresariales usando IA y procesamiento de lenguaje natural. El perfil se expresa como un vector de competencias con pesos numéricos, útil para comparar candidatos y puestos.

---

## Estructura del proyecto

```
AI_for_job_qualities/
├── requirements.txt
├── SPEC_PERFIL_AI.md         # Este documento
└── src/
    ├── main.py               # Entrada principal
    ├── analyzer/
    │    ├── text_cleaner.py      # Limpieza de texto
    │    ├── keyword_extractor.py # Extracción de keywords
    │    ├── embedding_matcher.py # Similitud semántica
    │    └── weight_assigner.py   # Asignación de pesos
    ├── data/
    │    └── skills_base.json     # Base de competencias
    └── utils/
         └── text_utils.py        # Funciones auxiliares
```

---

## Flujo de funcionamiento

1. **Carga de competencias**
   - Se lee el archivo `skills_base.json` con las competencias y sus keywords.

2. **Recepción de respuestas**
   - El sistema recibe un diccionario con la descripción del puesto y prioridades.

3. **Limpieza de texto**
   - Se normaliza el texto (minúsculas, sin signos, sin stopwords) usando `text_cleaner.py`.

4. **Extracción de keywords**
   - Se extraen palabras clave relevantes del texto usando spaCy en `keyword_extractor.py`.

5. **Comparación semántica**
   - Se calcula la similitud entre las keywords extraídas y las keywords de cada competencia usando embeddings (sentence-transformers) en `embedding_matcher.py`.

6. **Asignación de pesos**
   - Se asigna un peso a cada competencia según la similitud y si fue marcada como prioridad, en `weight_assigner.py`.

7. **Generación del perfil**
   - El resultado es un diccionario `{competencia: peso}` con valores entre 0 y 1.

8. **Salida**
   - El perfil se imprime en formato JSON, listo para comparar con candidatos.

---

## Ejemplo de entrada y salida

**Entrada:**
```python
respuestas = {
    "descripcion": "Buscamos un comercial B2B con buena comunicación, persistente y enfocado en resultados.",
    "prioridades": ["Cierre de ventas", "Comunicación", "Resiliencia"]
}
```

**Salida:**
```json
{
  "Comunicación": 0.9,
  "Cierre de ventas": 1.0,
  "Resiliencia": 0.8,
  "Empatía": 0.6,
  "Organización": 0.7
}
```

---

## Tecnologías usadas
- Python 3.11+
- sentence-transformers
- scikit-learn
- numpy, pandas
- fastapi (opcional para API)
- nltk, spacy
- pytest (pruebas)

---

## Extensiones y mejoras
- Puedes agregar un endpoint API con FastAPI para recibir las respuestas por HTTP.
- Puedes crear scripts de matching para comparar perfiles de empresa y candidatos.
- El sistema es modular y fácil de ampliar con nuevas competencias o lógica de ponderación.

---

## Notas
- El sistema está preparado para texto en español e inglés.
- Los pesos se normalizan entre 0 y 1.
- El código es fácil de integrar con motores de matching y otros sistemas de reclutamiento.

---

## Contacto y soporte
Para dudas o mejoras, consulta la documentación de cada módulo y los comentarios en el código.
