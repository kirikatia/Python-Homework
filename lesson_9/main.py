from aiogram.utils import executor
from config import dp
from commands import *

async def bot_start(_):
    print('Бот запущен')

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=bot_start)
