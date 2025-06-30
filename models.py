from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class History(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    language: str
    voice: str
    timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        table = True


class Favorite(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    language: str
    voice: str
    timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        table = True


class Config:
    orm_mode = True
    

HISTORY_TABLE = "history"
FAVORITES_TABLE = "favorites"

# Esquema general para futuras validaciones o migraciones
table_schemas = {
    HISTORY_TABLE: ["id", "text", "language", "voice", "timestamp"],
    FAVORITES_TABLE: ["id", "text", "language", "voice", "timestamp"]
}

