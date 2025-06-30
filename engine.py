from sqlmodel import create_engine

DATABASE_URL = "postgresql://user:password@localhost:5432/tts_db"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)
    print("Database initialized successfully.")
    