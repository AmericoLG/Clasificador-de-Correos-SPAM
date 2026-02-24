from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
from src.text_processor import TextProcessor
from src.spam_model import SpamModel

app = FastAPI()

# Permitir que React (Frontend) se comunique con Python (Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializamos las clases del diagrama [cite: 66]
processor = TextProcessor()
model = SpamModel()

# Cargar el modelo y vectorizador entrenados (RF-05) 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'models', 'spam_classifier.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'models', 'vectorizer.pkl')

if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    model.classifier = joblib.load(model_path)
    processor.vectorizer = joblib.load(vectorizer_path)
    print("✅ Modelo y Vectorizador cargados correctamente.")
else:
    print("⚠️ Advertencia: No se encontraron modelos entrenados.")

class MessageInput(BaseModel):
    text: str

@app.post("/predict")
async def predict(input_data: MessageInput):
    try:
        # 1. Preprocesar el texto recibido (RF-02) [cite: 42]
        clean_text = processor.remove_noise(input_data.text)
        
        # 2. Convertir a formato numérico
        vectorized_text = processor.vectorizer.transform([clean_text])
        
        # 3. Realizar la predicción (RF-04) [cite: 44]
        resultado = model.predict(vectorized_text)
        
        # 4. Calcular nivel de confianza (RI-03) [cite: 29]
        confianza = model.predict_proba(vectorized_text)
        
        return {
            "mensaje": input_data.text,
            "resultado": resultado,
            "confianza": round(confianza, 2)
        }
    except Exception as e:
        # Gestión de errores (RI-04) [cite: 31]
        raise HTTPException(status_code=500, detail=str(e))