"""
Módulo para limpieza y normalización de texto.
"""
import re
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

STOPWORDS = set(stopwords.words('spanish')) | set(stopwords.words('english'))

def limpiar_texto(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    tokens = texto.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return ' '.join(tokens)
