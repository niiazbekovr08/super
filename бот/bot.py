# import asyncio
# from aiogram import Bot, dispatcher, types
# from aiogram.filters import Command


# API_TOKEN = '8388571441:AAGcieMYQ9r2rvHJM-WifkR_tH5Dn8hOLKU'

# bot = Bot(token=API_TOKEN)
# from aiogram import Dispatcher

# dp = Dispatcher()

# @dp.message()
# async def echo(message: types.message):
#     await message.answer("Приветствую мой повелитель🫡")



# @dp.message()  
# async def echo(message: types.message):
#     await message.answer(f'Ты написал {message.text}')





# async def main():
#     await dp.start_polling(bot)




# if __name__=="_main_":
#     asyncio.run(main())
  

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = '8388571441:AAGcieMYQ9r2rvHJM-WifkR_tH5Dn8hOLKU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class OrderFSM(StatesGroup):
    name = State()
    order = State()
    time = State()
    edit_id = State()
    edit_field = State()
    edit_value = State()
    delete_id = State()

orders = {}
order_counter = 1

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить заказ")],
        [KeyboardButton(text="📖 Посмотреть заказы")],
        [KeyboardButton(text="✏ Изменить заказ")],
        [KeyboardButton(text="❌ Удалить заказ")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Здарова 😎", reply_markup=keyboard)

@dp.message(Command("basket"))
async def basket(message: types.Message):
    await message.answer("Корзина 🛒", reply_markup=keyboard)

@dp.message(lambda m: m.text == "➕ Добавить заказ")
async def add_order(message: types.Message, state: FSMContext):
    await state.set_state(OrderFSM.name)
    await message.answer("Как вас зовут?")

@dp.message(OrderFSM.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(OrderFSM.order)
    await message.answer("Что вы хотите заказать?")

@dp.message(OrderFSM.order)
async def get_order(message: types.Message, state: FSMContext):
    await state.update_data(order=message.text)
    await state.set_state(OrderFSM.time)
    await message.answer("К какому времени привезти заказ?")

@dp.message(OrderFSM.time)
async def get_time(message: types.Message, state: FSMContext):
    global order_counter
    data = await state.get_data()
    orders[order_counter] = {
        "name": data["name"],
        "order": data["order"],
        "time": message.text
    }
    await message.answer(f"Заказ добавлен. ID: {order_counter}")
    order_counter += 1
    await state.clear()

@dp.message(lambda m: m.text == "📖 Посмотреть заказы")
async def show_orders(message: types.Message):
    if not orders:
        await message.answer("Заказов нет")
        return
    text = ""
    for oid, o in orders.items():
        text += f"ID: {oid}\nИмя: {o['name']}\nЗаказ: {o['order']}\nВремя: {o['time']}\n\n"
    await message.answer(text)

@dp.message(lambda m: m.text == "❌ Удалить заказ")
async def delete_order(message: types.Message, state: FSMContext):
    await state.set_state(OrderFSM.delete_id)
    await message.answer("Введите ID заказа")

@dp.message(OrderFSM.delete_id)
async def confirm_delete(message: types.Message, state: FSMContext):
    try:
        oid = int(message.text)
        if oid in orders:
            del orders[oid]
            await message.answer("Заказ удалён")
        else:
            await message.answer("Заказ не найден")
    except:
        await message.answer("Введите число")
    await state.clear()

@dp.message(lambda m: m.text == "✏ Изменить заказ")
async def edit_order(message: types.Message, state: FSMContext):
    await state.set_state(OrderFSM.edit_id)
    await message.answer("Введите ID заказа")

@dp.message(OrderFSM.edit_id)
async def get_edit_id(message: types.Message, state: FSMContext):
    try:
        oid = int(message.text)
        if oid not in orders:
            await message.answer("Заказ не найден")
            await state.clear()
            return
        await state.update_data(oid=oid)
        await state.set_state(OrderFSM.edit_field)
        await message.answer("Что изменить? (name / order / time)")
    except:
        await message.answer("Введите корректный ID")

@dp.message(OrderFSM.edit_field)
async def get_edit_field(message: types.Message, state: FSMContext):
    if message.text not in ["name", "order", "time"]:
        await message.answer("name / order / time")
        return
    await state.update_data(field=message.text)
    await state.set_state(OrderFSM.edit_value)
    await message.answer("Введите новое значение")

@dp.message(OrderFSM.edit_value)
async def set_new_value(message: types.Message, state: FSMContext):
    data = await state.get_data()
    orders[data["oid"]][data["field"]] = message.text
    await message.answer("Данные обновлены")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
