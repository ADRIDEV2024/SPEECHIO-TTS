import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("La clave de API de OpenAI no está configurada. Por favor, establece la variable de entorno OPENAI_API_KEY.")


def generate_tts_audio(text: str, language: str, voice: str) -> bytes:
    """
    Llama a la API de OpenAI TTS para generar audio a partir de texto.
    """
    try:
        response = openai.audio.speech.create(
            model="tts-multilingual",
            input=text,
            voice=voice,
            response_format="mp3"
        )
        return response.read()
    except Exception as e:
        raise RuntimeError(f"Error al generar audio: {e}")
    


