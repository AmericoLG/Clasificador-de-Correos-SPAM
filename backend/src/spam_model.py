import joblib # Para la persistencia del modelo [cite: 24, 47]
from sklearn.naive_bayes import MultinomialNB

class SpamModel:
    def __init__(self):
        # Atributos según el diagrama de clases 
        self.classifier = MultinomialNB()
        self.metrics = {}

    def train(self, X, y):
        """Entrena el modelo supervisado [cite: 43, 82]"""
        self.classifier.fit(X, y)
        print("Modelo entrenado exitosamente.")

    def predict(self, text_vector):
        """Predice si es Spam o No Spam y devuelve la categoría [cite: 44, 83]"""
        prediction = self.classifier.predict(text_vector)
        # RF-04: Predicción de categoría [cite: 44]
        return "Spam" if prediction[0] == 1 else "No Spam"

    def predict_proba(self, text_vector):
        """Calcula el nivel de confianza (RI-03) [cite: 29, 76]"""
        probabilities = self.classifier.predict_proba(text_vector)
        return max(probabilities[0]) * 100

    def save_model(self, file_path):
        """Guarda el modelo para uso posterior (RF-05) [cite: 24, 47, 84]"""
        joblib.dump(self.classifier, file_path)

    def load_model(self, file_path):
        """Carga un modelo existente [cite: 47, 85]"""
        self.classifier = joblib.load(file_path)