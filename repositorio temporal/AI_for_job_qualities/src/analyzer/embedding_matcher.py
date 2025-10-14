"""
Módulo para comparación semántica usando embeddings.
"""
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

def obtener_similitud(keywords, skill_keywords):
    emb1 = model.encode(keywords, convert_to_tensor=True)
    emb2 = model.encode(skill_keywords, convert_to_tensor=True)
    sim = util.cos_sim(emb1, emb2)
    return float(sim.max())
