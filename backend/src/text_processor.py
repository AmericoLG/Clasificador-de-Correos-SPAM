import re
from sklearn.feature_extraction.text import TfidfVectorizer

class TextProcessor:
    def __init__(self):
        self.stopwords = {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'un', 'con'} 
        self.vectorizer = TfidfVectorizer()

    def remove_noise(self, text):
        """Limpia caracteres especiales y pasa a minúsculas [cite: 79]"""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text) 
        return text

    def tokenize(self, text):
        """Divide el texto y filtra palabras irrelevantes [cite: 79]"""
        words = text.split()
        return [w for w in words if w not in self.stopwords]

    def fit_transform(self, data):
        """Convierte una lista de textos en una matriz numérica [cite: 79]"""
        return self.vectorizer.fit_transform(data)
    
    def transform(self, data):
        """Transforma nuevos datos usando el vectorizador ya entrenado"""
        return self.vectorizer.transform(data)