FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /code/app

COPY entrypoint.sh esperar_banco.py /code/
RUN chmod +x /code/entrypoint.sh

EXPOSE 8080

CMD ["/code/entrypoint.sh"]