import asyncio
import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Получаем токен бота и ID канала из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения, bredrin!")
if not CHANNEL_ID:
    raise ValueError("CHANNEL_ID не найден в переменных окружения, mon!")

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_subscription_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру с кнопками подписки и проверки"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🌴 Подписаться на канал, mon!",
                    url=f"https://t.me/ViktorBitcoin"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔥 Проверить подписку, bredrin!",
                    callback_data="check_subscription"
                )
            ]
        ]
    )

async def check_subscription(user_id: int) -> bool:
    """Проверка подписки пользователя на канал, mon!"""
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        # Пользователь подписан, если не покинул канал и не исключен, ya feel me?
        return member.status not in ['left', 'kicked']
    except TelegramBadRequest as e:
        logging.error(f"Ошибка при проверке подписки для пользователя {user_id}, bredrin: {e}")
        return False
    except Exception as e:
        logging.error(f"Неожиданная ошибка при проверке подписки, mon: {e}")
        return False

@dp.message(CommandStart())
async def start_handler(message: Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    
    # Проверяем подписку на канал
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        # Отправляем голосовое сообщение после успешной регистрации
        voice_file = FSInputFile("2025-07-07 15.05.54.ogg")
        await message.answer_voice(voice=voice_file)
    else:
        await message.answer(
            f"🌴 Yo bredrin! Чтобы использовать Bombaclat GPT, нужно подписаться на канал @ViktorBitcoin, ya feel me?\n\n"
            "После подписки нажми кнопку 'Проверить подписку', mon!",
            reply_markup=get_subscription_keyboard()
        )

@dp.callback_query(F.data == "check_subscription")
async def check_subscription_callback(callback: CallbackQuery):
    """Обработчик кнопки проверки подписки"""
    user_id = callback.from_user.id
    
    # Проверяем подписку на канал
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        # Отправляем голосовое сообщение после успешной проверки
        voice_file = FSInputFile("2025-07-07 15.05.54.ogg")
        await callback.message.answer_voice(voice=voice_file)
        await callback.message.edit_text("✅ Проверка прошла успешно, mon!")
        await callback.answer("Проверка прошла успешно, mon!")
    else:
        await callback.answer("❌ Ты еще не подписался на канал, bredrin! Подпишись и попробуй снова, ya feel me?", show_alert=True)

@dp.message()
async def all_messages_handler(message: Message):
    """Обработчик всех остальных сообщений"""
    user_id = message.from_user.id
    
    # Проверяем подписку перед ответом
    is_subscribed = await check_subscription(user_id)
    
    if is_subscribed:
        await message.answer("Bomboclaat 🔥")
    else:
        await message.answer(
            f"🌴 Yo bredrin! Чтобы использовать Bomboclat GPT, нужно подписаться на канал @ViktorBitcoin, ya feel me?\n\n"
            "После подписки нажми кнопку 'Проверить подписку', mon!",
            reply_markup=get_subscription_keyboard()
        )

async def main():
    """Основная функция запуска бота"""
    print("🏝️ Запускаем бота Bombaclat, mon...")
    print(f"🌴 Канал для проверки подписки: {CHANNEL_ID}")
    
    while True:
        try:
            print("🔄 Подключаемся к Telegram API...")
            await dp.start_polling(bot)
        except Exception as e:
            print(f"❌ Бот упал, bredrin: {e}")
            print("🔄 Перезапускаем через 5 секунд...")
            await asyncio.sleep(5)
        finally:
            try:
                await bot.session.close()
            except:
                pass

if __name__ == "__main__":
    asyncio.run(main()) 