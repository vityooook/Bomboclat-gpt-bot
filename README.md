# 🏝️ Bombaclat Telegram Bot

Yo bredrin! Телеграм бот с проверкой подписки на канал, ya feel me? 🔥

## 🌴 Функционал, mon!

- При команде `/start` проверяет подписку пользователя на указанный канал, bredrin
- Если пользователь не подписан, предлагает подписаться и предоставляет кнопку для проверки, ya feel me?
- После успешной проверки подписки отправляет голосовое сообщение и на любое сообщение отвечает "Bombaclatt, mon! 🔥"

## 🎯 Настройка, bredrin!

1. Создайте файл `.env` на основе `config.env.example`, mon:
```bash
cp config.env.example .env
```

2. Отредактируйте `.env` файл, ya feel me?:
- `BOT_TOKEN` - токен вашего бота от @BotFather
- `CHANNEL_ID` - ID канала в формате -100

## 🐳 Запуск через Docker (рекомендуется), mon!

1. Убедитесь, что у вас установлен Docker и Docker Compose, bredrin

2. Постройте и запустите контейнер, ya feel me?:
```bash
docker-compose up -d
```

3. Для просмотра логов, mon:
```bash
docker-compose logs -f bombaclat-bot
```

4. Для остановки, bredrin:
```bash
docker-compose down
```

## 💻 Локальный запуск, bredrin!

1. Создайте виртуальное окружение, mon:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

2. Установите зависимости, ya feel me?:
```bash
pip install -r requirements.txt
```

3. Запустите бота, bredrin:
```bash
python bot.py
```

## 📁 Структура проекта, mon!

```
Bombaclat_bot/
├── bot.py                 # Основной код бота, bredrin
├── requirements.txt       # Python зависимости, ya feel me?
├── config.env.example     # Пример конфигурации, mon
├── 2025-07-07 15.05.54.ogg # Голосовое сообщение для успешной регистрации 🔥
├── Dockerfile            # Docker образ, bredrin
├── docker-compose.yml    # Docker Compose конфигурация, mon
├── .dockerignore         # Исключения для Docker, ya feel me?
└── README.md            # Документация, bredrin
```

## ⚠️ Важные требования, bredrin!

⚠️ **ОБЯЗАТЕЛЬНО**: Бот должен быть добавлен в канал как администратор для проверки подписки пользователей, ya feel me?!

## 🎵 Примечания, mon!

- Канал должен быть публичным или бот должен иметь доступ к нему, bredrin
- Логи сохраняются в папку `logs/` при запуске через Docker, mon
- При первом запуске убедитесь, что канал указан правильно (например: @ViktorBitcoin), ya feel me?
- Бот автоматически перезапускается при падении, bredrin! 🔄 