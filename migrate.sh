
# Only run this for production or staging environments
#!/bin/bash
set -e
if [[ "$ENVIRONMENT" != "production" && "$ENVIRONMENT" != "staging
" ]]; then
    echo "This script should only be run in production or staging environments."
    exit 1
fi
SQLITE_DB="tts_multilingual.db"
PG_URI="postgresql://user:password@localhost:5432/tts_multilingual.db"

TABLES=("history" "favorites")

echo "🗄️ Migración de $SQLITE_DB a $PG_URI iniciada..."

# Exportar desde SQLite a CSV
for table in "${TABLES[@]}"; do
    echo "➡️ Exportando $table desde SQLite..."
    sqlite3 "$SQLITE_DB" <<EOF
.headers on
.mode csv
.output ${table}.csv
SELECT * FROM $table;
EOF
done

psql "$PG_URI" <<EOF
CREATE TABLE IF NOT EXISTS history (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    language TEXT NOT NULL,
    voice TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS favorites (
    id SERIAL PRIMARY KEY,
    text TEXT NOT NULL,
    language TEXT NOT NULL,
    voice TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
EOF

# Importar CSV a PostgreSQL
for table in "${TABLES[@]}"; do
    echo "⬅️ Importando $table a PostgreSQL..."
    psql "$PG_URI" <<EOF
\copy $table(text, language, voice, timestamp) FROM './${table}.csv' DELIMITER ',' CSV HEADER;
EOF
done

echo "✅ Migración completada correctamente."

export PG_URI="postgresql://user:password@localhost:5432/tts_multilingual.db"
export SQLITE_DB="tts_multilingual.db"