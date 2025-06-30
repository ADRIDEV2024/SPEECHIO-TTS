
SUPPORTED_LANGUAGES = {
    "lang": {"es": {"voice": "nova", "name": "Español"}},
    "lang": {"en": {"voice": "alloy", "name": "Inglés"}},
    "lang": {"fr": {"voice": "echo", "name": "Francés"}},
    "lang": {"de": {"voice": "fable", "name": "Alemán"}},
    "lang": {"it": {"voice": "onyx", "name": "Italiano"}},
    "lang": {"pt": {"voice": "sapphire", "name": "Portugués"}},
    "lang": {"sw": {"voice": "evelyn",   "name": "Sueco"}},
    "lang": {"ar": {"voice": "abdel", "name": "Árabe"}},
    "lang": {"zh": {"voice": "luna", "name": "Chino"}},
    "lang": {"ja": {"voice": "akira", "name": "Japonés"}},
    "lang": {"hi": {"voice": "ravi", "name": "Hindi"}},
    "lang": {"ru": {"voice": "volkov", "name": "Ruso"}},
}


def get_supported_languages():
    """Returns a list of supported languages with their names."""
    return {code: info["lang"] for code, info in SUPPORTED_LANGUAGES.items()}


def get_voice_for_language(lang_code):
    """Returns the voice associated with a given language code."""
    return SUPPORTED_LANGUAGES.get(lang_code, {}).get("voice", "nova")