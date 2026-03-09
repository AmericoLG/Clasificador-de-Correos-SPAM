import pandas as pd
import joblib
import os
from src.text_processor import TextProcessor
from src.spam_model import SpamModel

# 1. Dataset Extendido (Más ejemplos = Mejor detección)
data = {
    'texto': [
        # Ejemplos de SPAM (Etiqueta 1)
        '¡Felicidades! Has ganado un premio de $10,000. Haz clic aquí',
        'Gana dinero rápido trabajando desde casa, sin experiencia',
        'URGENTE: Tu cuenta ha sido bloqueada, ingresa tus datos ahora',
        'Has sido seleccionado como el ganador de un premio de $1,000,000. Haz clic aquí',
        'Pierde 10 kilos en una semana con nuestras pastillas mágicas naturales',
        'Invierta $200 en Bitcoin hoy y reciba $2,000 en menos de 24 horas',
        'Oferta limitada: compra ya con 80% de descuento en nuestra tienda',
        'Gane dinero desde casa trabajando solo 2 horas al día. Regístrese hoy',
        'Su cuenta bancaria tiene actividad sospechosa. Verifique su identidad aquí',
        'Préstamos inmediatos sin revisión de crédito. Solicite su dinero ya',
        
        # Ejemplos de NO SPAM / HAM (Etiqueta 0)
        'Hola, ¿confirmamos la reunión para mañana a las 10?',
        'Tu código de verificación para la cuenta es 4455',
        'El reporte mensual ya está listo en la carpeta compartida',
        'Hola equipo, les adjunto el acta de la reunión de hoy',
        'Tu pedido de comida está en camino y llegará en 15 minutos',
        '¿Qué tal? Te escribía para confirmar la cena de mañana',
        'Estimado estudiante, la entrega del proyecto es el próximo lunes',
        'Hola, solicitaste un cambio de contraseña en tu plataforma',
        'Te envié los documentos que me pediste por correo ayer',
        '¿Podemos vernos en la oficina para revisar el presupuesto?'
    ],
    'etiqueta': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# 2. Inicializar componentes
processor = TextProcessor()
model = SpamModel()

# 3. Preprocesamiento (RF-02)
textos_limpios = [processor.remove_noise(t) for t in df['texto']]

# 4. Ajustar Vectorizador (Vital para capturar palabras clave como "dinero", "clic", "reunión")
X = processor.vectorizer.fit_transform(textos_limpios)
y = df['etiqueta']

# 5. Entrenamiento (RF-03)
model.train(X, y)

# 6. Guardar Modelo y Vectorizador (RF-05/06)
if not os.path.exists('models'):
    os.makedirs('models')

joblib.dump(model.classifier, 'models/spam_classifier.pkl')
joblib.dump(processor.vectorizer, 'models/vectorizer.pkl')

print(f"✅ Entrenamiento completado con {len(df)} ejemplos.")
print("Archivos guardados en /models")