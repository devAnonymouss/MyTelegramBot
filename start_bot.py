from aiogram.utils import executor
from create_bot import dp
from date_base import sqlite_db


from handlers import client
client.register_handlers_client(dp)


async def on_startup(_):
    print("Бот вышел в онлайн")
    sqlite_db.sql_start()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)