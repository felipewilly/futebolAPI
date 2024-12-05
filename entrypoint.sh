#!/bin/sh

echo "Aguardando o Postgres..."

python /code/esperar_banco.py

echo "Postgres iniciado"

alembic revision --autogenerate -m "Migration auto"
alembic upgrade head

exec /usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port 8080
