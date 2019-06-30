FROM python:3.7.2-alpine
RUN pip install poetry
COPY . /app
WORKDIR /app
RUN poetry install && poetry run tox -e py37
EXPOSE 8080
CMD ["poetry", "run", "python", "main.py"]
