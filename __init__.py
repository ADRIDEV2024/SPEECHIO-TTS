from .tts_engine import generate_tts_audio
from .language_config import SUPPORTED_LANGUAGES

__all__ = [
    "generate_tts_audio",
    "SUPPORTED_LANGUAGES"
]


class TTSConfig:
    def __init__(self, language: str = "lang", voice: str = "voice"):
        self.language = language
        self.voice = voice

    def get_voice(self):
        return SUPPORTED_LANGUAGES.get(self.language, {}).get("voice", self.voice)

    def get_language_name(self):
        return SUPPORTED_LANGUAGES.get(self.language, {}).get("name", "Unknown Language")
    
    def is_supported(self):
        return self.language in SUPPORTED_LANGUAGES
    
    def __str__(self):
        return f"TTSConfig(language={self.language}, voice={self.voice})"


class TTSException(Exception):
    """Base exception for TTS errors."""
    pass

