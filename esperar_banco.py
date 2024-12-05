import psycopg2
from time import sleep
from os import environ

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=environ['POSTGRES_DB'],
                user=environ['POSTGRES_USER'],
                password=environ['POSTGRES_PASSWORD'],
                host='db'
            )
            conn.close()
            return
        except psycopg2.OperationalError:
            print("Banco de dados não está disponível, esperando 1 segundo...")
            sleep(1)

if __name__ == "__main__":
    wait_for_db()
