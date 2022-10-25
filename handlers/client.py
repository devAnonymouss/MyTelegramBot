from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from date_base import sqlite_db

import asyncio

#@dp.message_handler(commands=['start'])
async def command_start(message:types.Message):
    await bot.send_message(message.from_user.id,'Привет! Меня создали,чтобы я напомнил тебе купить хлеб и поздравить бабушку с ДР.', reply_markup=kb_client)
    await message.delete()

class FSMClient(StatesGroup):
    notification = State()
    times = State()

# @dp.message_handler(commands='Добавить_уведомление', state=None)
async def cm_start(message : types.Message):
    await FSMClient.notification.set()
    await message.reply('Напиши о чём тебе напомнить')

# @dp.message_handler(content_types=['notification'], state=FSMClient.notification)
async def add_notification(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['notification'] = message.text
    await FSMClient.next()
    await message.reply('Через сколько минут тебе напомнить?')

# @dp.message_handler(state=FSMClient.times)
async def add_time(message: types.Message, state: FSMContext):
    async with state.proxy() as date:
        date['times'] = int(message.text)
        await message.reply('Время пошло')
    async def eternity():
        await asyncio.sleep(date['times'])
        await message.reply(date['notification'])


    await sqlite_db.sql_add_command(state)
    await state.finish()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(cm_start, commands=['Добавить_уведомление'], state=None)
    dp.register_message_handler(add_notification, state=FSMClient.notification)
    dp.register_message_handler(add_time, state=FSMClient.times)

if __name__ == '__main__':
    asyncio.run(eternity())


