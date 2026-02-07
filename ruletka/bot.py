import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from game import RussianRouletteGame

TOKEN ="8047711592:AAGLwPUxO0l2lL8l72p_LtV4AjPciLfbTSE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

game = None

# --- /start ---
@dp.message(Command("start"))
async def start(message: types.Message):
    global game
    game = RussianRouletteGame("roma", "suli")

    await message.answer(
        "🎮 Русская рулетка\n\n"
        "Игроки:\n"
        "👤 Игрок 1\n"
        "👤 Игрок 2\n\n"
        "Команды:\n"
        "/shot — выстрел\n"
        "/stop — закончить игру\n\n"
        f"Первый ход: Игрок 1\n"
        "⏱ У вас 5 секунд!"
    )

# --- /shoot ---
@dp.message(Command("shot"))
async def shot(message: types.Message):
    global game

    if not game:
        await message.answer("Сначала запусти игру: /start")
        return

    result = game.shoot()
    await message.answer(result)

    if game.is_game_over:
        await message.answer(game.get_result())
        game = None

# --- /stop ---
@dp.message(Command("stop"))
async def stop(message: types.Message):
    global game

    if not game:
        await message.answer("Игра не запущена")
        return

    game.stop()
    await message.answer("⛔ Игра остановлена вручную")
    await message.answer(game.get_result())
    game = None

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
