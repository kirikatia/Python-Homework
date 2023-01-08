from config import dp, bot
from aiogram import types
from bot_ai import make_move
from random import randint

# Начальное количество конфет
TOTAL = 150
# Объект для подсчета количества конфет для разных пользователей
# ключ - user id
# значение - текущее кол-во конфет
user_total = {}

@dp.message_handler(commands='start')
async def starting(message: types.Message):
    global user_total
    user_total[message.from_user.id] = TOTAL

    await bot.send_message(message.from_user.id,
        f'Игра в конфеты. На столе лежит {TOTAL} конфет.\n' +
        'Игроки ходят по очереди.\n' +
        'За ход можно взять 1-28 конфет.\n' +
        'Игрок взявший последнюю конфету побеждает.\n'
    )

    if randint(1, 2) == 1:
        await bot.send_message(message.from_user.id, 'Вы ходите первым, введите количество конфет:')
        return
    
    await bot.send_message(message.from_user.id, 'Я хожу первым.')
    await send_made_move_message(message, 'Я', make_move(user_total[message.from_user.id]))


@dp.message_handler()
async def all_messages(message: types.Message):
    global user_total
    
    if message.from_user.id not in user_total:
        await bot.send_message(message.from_user.id, 'Введите /start, чтобы узнать правила и начать игру')
        return

    if not message.text.isnumeric():
        await message.reply('Введите число от 1 до 28, либо введите команду /start, чтобы перезапустить игру')
        return

    take = int(message.text)
    if take <= 0 or take > 28:
        await message.reply(f'{message.from_user.first_name}, пожалуйста введите число от 1 до 28')
        return

    win = await send_made_move_message(message, message.from_user.first_name, take)
    if not win:
        await send_made_move_message(message, 'Я', make_move(user_total[message.from_user.id]))

async def send_made_move_message(message, who, take):
    if take >= user_total[message.from_user.id]:
        await bot.send_message(message.from_user.id, f'{who} забрал все оставшиеся конфеты и победил!')
        await bot.send_message(message.from_user.id, 'Введите /start, чтобы сыграть ещё раз')
        del user_total[message.from_user.id]
        return True

    user_total[message.from_user.id] -= take
    await bot.send_message(message.from_user.id, f'{who} взял {take} конфет и на столе осталось {user_total[message.from_user.id]} конфет.')
    return False