# Используем базовый образ Python
FROM python:3.11

RUN mkdir /app

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем только файлы, необходимые для установки зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi


COPY . .

# Запускаем сервер при запуске контейнера
CMD ["python", "main.py"]