run:
    uvicorn app.main:app --reload

migration:
    alembic revision --autogenerate -m "Migration auto"

migrate:
    alembic upgrade head