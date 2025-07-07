# Используем официальный Python образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения и голосовые файлы
COPY bot.py .
COPY *.ogg .

# Указываем команду для запуска
CMD ["python", "bot.py"] 