# 🌍✍👅🔊 SPEECHIO-TTS: Text-to-Speech Multilingüe

Convierte texto en audio en múltiples idiomas de forma sencilla, rápida y divertida. Este proyecto aprovecha Streamlit, OpenAI TTS y LangChain para ofrecer una experiencia moderna de síntesis de voz multilingüe, con historial, favoritos, ejemplos y traducción automática.

---

## Tabla de Contenidos

- [Características principales](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Inicialización y Uso](#inicialización-y-uso)
- [Detalles de Carpetas y Archivos](#detalles-de-carpetas-y-archivos)
- [Contribuye](#contribuir)

---

## Características principales

- **Soporte Multilingüe:** Convierte texto a voz en hasta 20 idiomas de todo el globo (español, inglés, francés, alemán, etc.).
  
- **Traducción Automática:** Traduce el texto de entrada al idioma seleccionado usando modelos LLM, inspirado de la forma en que ElevenLabs o Natural Reader lo hacen.
  
- **Historial y Favoritos:** Guarda y consulta tus conversiones recientes y frases favoritas.
  
- **Ejemplos por Categoría:** Accede a frases de ejemplo organizadas por temas e idiomas.


  ## Estructura del Proyecto
```
SPEECHIO-TTS/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── db/
│   ├── __init__.py
│   ├── engine.py
│   ├── models.py
│   ├── persistance.py
│   └── tts_multilingual.db
│
├── tts/
│   ├── __init__.py
│   ├── tts_engine.py
│   └── language_config.py
│
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── prompt_loader.py
│
└── data/
    └── prompts/
        ├── basics/
        │   ├── en.txt
        │   ├── es.txt
        │   ├── fr.txt
        │   └── de.txt
        |   └── ...
        ├── bussiness/
        |   └── ...
        ├── tech/
        |   └── ...
        └── travel/
            └── ...
```
---

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/ADRIDEV2024/SPEECHIO-TTS.git
   cd SPEECHIO-TTS

2. Crea un entorno virtual (yo utilo venv en la mayoría de los casos) y actívalo:
  ```sh
python -m venv venv
venv\Scripts\activate   # En Windows
source venv/bin/activate  # En Linux/Mac
 ```

3. Instala las dependencias del proyecto:
```sh
pip install -r requirements.txt
```
4. Configura tus variables de entorno con .env en la raíz con tu apikey de OpenAI:
```sh
OPENAI_API_KEY=tu_clave_openai
```
## Inicialización y Uso


1. Inicializa la base de datos (opcional, solo la primera vez):
```sh
python -c "from db import init_db; init_db()"
```
2. Ejecuta la aplicación:
```sh
streamlit run app.py
```
3. **¡Listo! Accede a la interfaz web que se abrirá en tu navegador.**
  
- **Caché de Audio:** Evita llamadas repetidas a la API almacenando los audios generados.
  
- **Descarga y Eliminación:** Descarga tus audios o elimina entradas del historial/favoritos.
- **Interfaz Web Moderna:** Todo gestionado desde una interfaz Streamlit intuitiva.

---

## Detalles de Carpetas y Archivos

app.py

Punto de entrada principal. Gestiona la interfaz Streamlit, interacción con el usuario, historial, favoritos, ejemplos y lógica de audio.

db/

models.py: Define los modelos de historial y favoritos.
persistance.py: Funciones CRUD para historial y favoritos usando SQLite.

engine.py: Motor de base de datos alternativo (PostgreSQL).

tts_multilingual.db: Base de datos PostgreSQL local (Producción).

tts/

tts_engine.py: Lógica para llamar a la API de OpenAI TTS.

language_config.py: Configuración de idiomas y voces soportadas.

__init__.py: Utilidades y clases para configuración TTS.
utils/

helpers.py: Funciones auxiliares para caché de audio y carga de ejemplos.

prompt_loader.py: Carga frases de ejemplo por categoría e idioma.

data/prompts/

Frases de ejemplo organizadas por categorías (basics, bussiness, tech, travel) y por idioma (en.txt, es.txt, etc.).
