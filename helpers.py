import os
import hashlib
from tts.tts_engine import generate_tts_audio


CACHE_DIR = ".cache/audio"
os.makedirs(CACHE_DIR, exist_ok=True)


def load_prompt_texts(language: str) -> list[str]:
    """Carga frases de ejemplo para un idioma dado."""
    path = f"data/prompts/{language}.txt"
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
    

def get_tts_cached(text: str, language: str, voice: str) -> bytes:
    """Genera o carga audio en caché si ya existe."""
    key = hashlib.sha256(f"{language}_{voice}_{text}".encode()).hexdigest()
    audio_path = os.path.join(CACHE_DIR, f"{key}.mp3")

    if os.path.exists(audio_path):
        with open(audio_path, "rb") as f:
            return f.read()
    else:
        audio_bytes = generate_tts_audio(text, language, voice)
        with open(audio_path, "wb") as f:
            f.write(audio_bytes)
        return audio_bytes


def list_cached_audios() -> list[str]:
    return [f for f in os.listdir(CACHE_DIR) if f.endswith(".mp3")]    


def clear_cache():
    for filename in os.listdir(CACHE_DIR):
        file_path = os.path.join(CACHE_DIR, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Caché de audio limpiada.")

