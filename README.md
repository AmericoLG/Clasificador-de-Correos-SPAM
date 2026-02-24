¡Excelente! Un buen **README** es la cara del proyecto y es fundamental para que cualquiera (o tú mismo en el futuro) sepa cómo echarlo a andar en segundos.

Aquí tienes un diseño profesional en Markdown que resume todo lo que hemos construido siguiendo tu documentación:

---

# 📧 Clasificador de Correos Spam

Este proyecto es un sistema de **Machine Learning supervisado** que utiliza el algoritmo **Multinomial Naive Bayes** para categorizar mensajes como **Spam** o **No Spam**. Cuenta con un backend robusto en Python y una interfaz moderna en React.

## 🚀 Estructura del Proyecto

* **Backend:** FastAPI, Scikit-learn, Pandas.
* **Frontend:** React, Axios.
* **ML:** Procesamiento de Lenguaje Natural (NLP) con TF-IDF.

---

## 🛠️ Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/AmericoLG/Clasificador-de-Correos-SPAM.git
cd Clasificador-de-Correos-SPAM

```

### 2. Configurar el Backend (Python)

Entra a la carpeta del servidor e instala las dependencias:

```bash
cd backend
python -m venv venv
# Activar venv:
# Windows: .\venv\Scripts\activate | Mac/Linux: source venv/bin/activate
pip install -r requirements.txt

```

### 3. Configurar el Frontend (React)

Abre una nueva terminal en la raíz del proyecto:

```bash
cd frontend
npm install

```

---

## 🧠 Entrenamiento del Modelo (Primeros Pasos)

Antes de iniciar la aplicación, es necesario generar el modelo entrenado (Persistencia RF-05). Hemos incluido un script con un **dataset de ejemplo** para inicializar el sistema:

1. Asegúrate de estar en la carpeta `backend` con el entorno virtual activo.
2. Ejecuta el script de entrenamiento:
```bash
python entrenar_inicial.py

```


*Esto creará la carpeta `/models` con los archivos `.pkl` necesarios para el clasificador.*

---

## 🏃 Ejecución del Proyecto

Para que el sistema funcione, ambos servidores deben estar corriendo simultáneamente:

### Iniciar Backend (API)

Desde la carpeta `backend`:

```bash
uvicorn src.main:app --reload

```

*El servidor estará disponible en `http://127.0.0.1:8000*`

### Iniciar Frontend (UI)

Desde la carpeta `frontend`:

```bash
npm start

```

*La interfaz se abrirá automáticamente en `http://localhost:3000*`

---

## 📊 Funcionalidades Completadas

* [x] **RF-01**: Carga de datos etiquetados (Script inicial).
* [x] **RF-02**: Preprocesamiento de texto (NLP).
* [x] **RF-03**: Entrenamiento del modelo Naive Bayes.
* [x] **RF-04**: Clasificación de correos en tiempo real.
* [x] **RI-03**: Visualización del nivel de confianza por predicción.
* [x] **RI-05**: Dashboard con estadísticas de análisis.

---
