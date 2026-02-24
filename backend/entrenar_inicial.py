import pandas as pd
import joblib
import os
from src.text_processor import TextProcessor
from src.spam_model import SpamModel

# 1. Crear Dataset de prueba (Basado en RF-01: Carga de Datos Etiquetados)
# 1 = Spam, 0 = No Spam (Ham)
data = {
    'texto': [
        '¡Felicidades! Has ganado un premio de $10,000. Haz clic aquí', # Ejemplo del Mockup
        'Hola, ¿confirmamos la reunión para mañana a las 10?',
        'Gana dinero rápido trabajando desde casa, sin experiencia',
        'Tu código de verificación para la cuenta es 4455',
        'URGENTE: Tu cuenta ha sido bloqueada, ingresa tus datos ahora',
        'El reporte mensual ya está listo en la carpeta compartida'
    ],
    'etiqueta': [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# 2. Inicializar componentes según el Diagrama de Clases
processor = TextProcessor()
model = SpamModel()

# 3. Preprocesamiento de Texto (RF-02)
# Limpiamos los textos antes de entrenar
textos_limpios = [processor.remove_noise(t) for t in df['texto']]

# 4. Ajustar el Vectorizador y transformar los datos
# Esto es vital para que el modelo entienda las palabras clave
X = processor.vectorizer.fit_transform(textos_limpios)
y = df['etiqueta']

# 5. Entrenamiento del Modelo (RF-03)
model.train(X, y)

# 6. Persistencia del Modelo (RF-05)
# Guardamos tanto el modelo como el vectorizador para que la API los use
if not os.path.exists('models'):
    os.makedirs('models')

joblib.dump(model.classifier, 'models/spam_classifier.pkl')
joblib.dump(processor.vectorizer, 'models/vectorizer.pkl')

print("✅ Entrenamiento completado. Archivos guardados en /models")