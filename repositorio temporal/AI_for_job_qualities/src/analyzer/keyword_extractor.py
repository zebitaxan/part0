"""
Módulo para extracción de palabras clave del texto.
"""
import spacy

try:
    nlp = spacy.load('es_core_news_sm')
except:
    nlp = spacy.load('en_core_web_sm')

def extraer_keywords(texto):
    doc = nlp(texto)
    keywords = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'PROPN', 'ADJ']]
    return keywords
