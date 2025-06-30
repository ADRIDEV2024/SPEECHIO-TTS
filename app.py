# File: app.py

import streamlit as st
import tts
from tts.tts_engine import generate_tts_audio
from utils.helpers import get_tts_cached, load_prompt_texts
from db.persistance import add_to_history, add_to_favorites, get_history, get_favorites
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from tts import language_config
from tts.language_config import SUPPORTED_LANGUAGES

st.set_page_config(page_title="TTS Multilingual App", layout="centered")
st.title("🌍 Text-to-Speech Multilingüe")
st.markdown("¡ Convierte texto a audio en múltiples idiomas con Streamlit y LangChain de la manera más simple posible !")

if "history" not in st.session_state:
    st.session_state.history = []
if "favorites" not in st.session_state:
    st.session_state.favorites = []

with st.sidebar:
    st.header("Configuración de Idioma")
    lang = st.selectbox("Selecciona un idioma", options=list(language_config.SUPPORTED_LANGUAGES))
    voice = language_config.SUPPORTED_LANGUAGES["voice"]

st.subheader("Ingresa texto para convertir en audio")
text_input = st.text_area("Texto", height=150)
translate = st.checkbox("Traducir al idioma seleccionado")

if st.button("🔊 Generar Audio"):
    if text_input.strip():
        if translate:
            llm = ChatOpenAI(temperature=0)
            prompt = f"Traduce este texto al idioma {lang}: {text_input}"
            translation = llm([HumanMessage(content=prompt)]).content
            st.info(f"Traducción: {translation}")
            final_text = translation
        else:
            final_text = text_input

        audio_bytes = get_tts_cached(final_text, lang, voice)
        st.audio(audio_bytes, format="audio/mp3")

        add_to_history(final_text, lang, voice)
        if st.button("⭐ Agregar a Favoritos", key="fav_button"): 
            add_to_favorites(final_text, lang, voice)
    else:
        st.warning("Por favor, introduce un texto primero.")

st.markdown("---")
st.subheader("Frases de ejemplo")
examples = load_prompt_texts(lang)
if examples:
    for i, line in enumerate(examples):
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(f"Escuchar: {line[:40]}...", key=f"ex_{i}"):
                audio_bytes = get_tts_cached(line, lang, voice)
                st.audio(audio_bytes, format="audio/mp3")
        with col2:
            if st.button("⭐", key=f"ex_fav_{i}"):
                add_to_favorites(line, lang, voice)

# FILTROS
st.markdown("---")
st.subheader("🔍 Buscar Historial y Favoritos")
search_text = st.text_input("Buscar por texto")
search_lang = st.selectbox("Filtrar por idioma", options=["todos"] + list(SUPPORTED_LANGUAGES.keys()))

# FUNCION DE FILTRADO SIMPLE

def match_entry(entry, keyword, lang_filter):
    text, lang, _ = entry
    if keyword.lower() in text.lower():
        if lang_filter == "todos" or lang_filter == lang:
            return True
    return False

# HISTORIAL
st.markdown("---")
st.subheader("🕓 Historial")
history = get_history(100)
filtered_hist = [e for e in history if match_entry(e, search_text, search_lang)]

for i, (text, l, v) in enumerate(filtered_hist):
    audio_bytes = get_tts_cached(text, l, v)
    st.write(f"{i+1}: {text} [{l}]")
    st.audio(audio_bytes, format="audio/mp3")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.download_button("📥 Descargar", audio_bytes, file_name=f"tts_{l}_{i}.mp3", mime="audio/mpeg", key=f"dl_hist_{i}")
    with col2:
        if st.button("🗑️ Eliminar", key=f"rm_hist_{i}"):
            # eliminar lógica opcional: pendiente de implementar en BD
            st.warning("(Simulado) Entrada eliminada del historial")

st.markdown("---")
st.subheader("⭐ Favoritos")
favorites = get_favorites()
filtered_favs = [e for e in favorites if match_entry(e, search_text, search_lang)]

for i, (text, l, v) in enumerate(filtered_favs):
    audio_bytes = get_tts_cached(text, l, v)
    st.write(f"{i+1}: {text} [{l}]")
    st.audio(audio_bytes, format="audio/mp3")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.download_button("📥 Descargar", audio_bytes, file_name=f"fav_tts_{l}_{i}.mp3", mime="audio/mpeg", key=f"dl_fav_{i}")
    with col2:
        if st.button("🗑️ Eliminar", key=f"rm_fav_{i}"):
            # eliminar lógica opcional: pendiente de implementar en BD
            st.warning("(Simulado) Entrada eliminada de favoritos")