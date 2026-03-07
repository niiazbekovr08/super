from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

TOKEN = "8675575050:AAGMw73r5jRHt2gFuKuJZQ3pv4l83Ivhd00"
CHANNEL_ID = -1003405175942

bot = Bot(token=TOKEN)
dp = Dispatcher()

messages = {}

# Обработчик сообщений
@dp.message()
async def handle_message(message: types.Message):
    if message.text == "/start":
        await message.answer("Привет! Это анонимный бот IUCA.\nОтправь сообщение и оно будет опубликовано анонимно.")
    else:
        # Создаем клавиатуру с кнопкой "Ответить" правильно
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Ответить", callback_data=f"reply_{message.from_user.id}")]
            ]
        )

        sent = await bot.send_message(
            CHANNEL_ID,
            f"📢 АНОН IUCA\n\n{message.text}",
            reply_markup=keyboard
        )
        messages[sent.message_id] = message.from_user.id
        await message.answer("✅ Сообщение отправлено анонимно!")

# Обработчик нажатий кнопки
@dp.callback_query()
async def handle_reply(callback: types.CallbackQuery):
    user_id = int(callback.data.split("_")[1])
    await bot.send_message(callback.from_user.id, "Напиши свой ответ. Он будет отправлен анонимно.")
    messages[callback.from_user.id] = user_id

# Обработчик анонимных ответов
@dp.message()
async def handle_anonymous_reply(message: types.Message):
    if message.from_user.id in messages:
        target = messages[message.from_user.id]
        await bot.send_message(target, f"📩 Анонимный ответ:\n\n{message.text}")
        await message.answer("✅ Ответ отправлен анонимно!")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())