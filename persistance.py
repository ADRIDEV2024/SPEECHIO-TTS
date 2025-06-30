import sqlite3
import os
from typing import List, Tuple
from db.models import HISTORY_TABLE, FAVORITES_TABLE


DB_PATH = os.path.join(os.path.dirname(__file__), 'tts_multilingual.db')


class DatabaseError(Exception):
    pass


def handle_db_operation(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as e:
            raise DatabaseError(f"Database error in {func.__name__}: {e}")
        except Exception as e:
            raise DatabaseError(f"Unexpected error in {func.__name__}: {e}")
    return wrapper


@handle_db_operation
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {HISTORY_TABLE} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        text TEXT,
                        language TEXT,
                        voice TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        )''')
                
        c.execute(f'''CREATE TABLE IF NOT EXISTS {FAVORITES_TABLE} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        text TEXT,
                        language TEXT,
                        voice TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')
        
        c.execute(f'''CREATE INDEX IF NOT EXISTS idx_history_timestamp ON {HISTORY_TABLE} (timestamp)''')
        c.execute(f'''CREATE INDEX IF NOT EXISTS idx_favorites_timestamp ON {FAVORITES_TABLE} (timestamp)''')
        conn.commit()


@handle_db_operation
def add_to_history(text: str, language: str, voice: str):
    validate_input(text, language, voice)
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(f'''INSERT INTO {HISTORY_TABLE} (text, language, voice) VALUES (?, ?, ?)", (text, language, voice)''')
        conn.commit()


@handle_db_operation
def add_to_favorites(text: str, language: str, voice: str):
    validate_input(text, language, voice)
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(f'''INSERT INTO {FAVORITES_TABLE} (text, language, voice) VALUES (?, ?, ?)", (text, language, voice)''')
        conn.commit()


@handle_db_operation
def get_history(limit: int = 100) -> List[Tuple[str, str, str]]:
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(f'''SELECT text, language, voice FROM {HISTORY_TABLE} ORDER BY timestamp DESC LIMIT ?", (limit,)''')
        return c.fetchall()


@handle_db_operation
def get_favorites() -> List[Tuple[str, str, str]]:
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(f'''SELECT text, language, voice FROM {FAVORITES_TABLE} ORDER BY timestamp DESC)''')
        return c.fetchall()


@handle_db_operation
def delete_from_history(text: str, language: str, voice: str):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(f'''DELETE FROM {HISTORY_TABLE} WHERE text = ? AND language = ? AND voice = ?", (text, language, voice)''')


@handle_db_operation
def delete_from_favorites(text: str, language: str, voice: str):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(f'''DELETE FROM {FAVORITES_TABLE} WHERE text = ? AND language = ? AND voice = ?", (text, language, voice)''')


def validate_input(text: str, language: str, voice: str):
    if not text or not text.strip():
        raise ValueError("Texto no puede estar vacío")
    if not language or not isinstance(language, str):
        raise ValueError("Idioma inválido")
    if not voice or not isinstance(voice, str):
        raise ValueError("Voz inválida")
    