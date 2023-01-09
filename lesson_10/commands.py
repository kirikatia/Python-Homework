from config import dp, bot
from aiogram import types
from aiogram.utils import deep_linking
from random import randint
import game_state

@dp.message_handler(commands='start')
async def starting(message: types.Message):
    # Обработка данных из ссылки-приглашения
    args = message.get_args()
    payload = deep_linking.decode_payload(args)

    # Если приглашение не пусто
    player = None
    if payload != '':
        player = int(payload)

    if game_state.find_game(message.from_user.id) is not None:
        await bot.send_message(message.from_user.id, 'Вы уже находитесь в игре с другим пользователем, если хотите остановить её, используйте команду /restart')
        return
        
    if not player:
        await send_start_message(
            message.from_user.id, 
            'Игра в крестики-нолики.\n'
        )
        return

    if game_state.find_game(player):
        await send_start_message(
            message.from_user.id, 
            'Данный пользователь уже играет в игру!\n' +
            'Дождитесь завершения партии, либо:'
        )
        return

    if player == message.from_user.id:
        await send_start_message(
            message.from_user.id, 
            'Нельзя играть с самим собой!\n'
        )
        return

    # Выбираем случайную очередность хода
    order = randint(1, 2)
    player1 = player if order == 1 else message.from_user.id
    player2 = player if order == 2 else message.from_user.id

    # Создаем объект с информацией о игре
    game = game_state.add_game(player1, player2)
    
    # Сообщаем игрокам о старте игры
    await bot.send_message(player1, 'Вы ходите первым:')
    await bot.send_message(player1, 'Делайте ваш ход:', reply_markup=make_board_markup(game['board']))
    await bot.send_message(player2, 'Вы ходите вторым, ожидайте хода соперника.')

async def send_start_message(who, text):
    await bot.send_message(who,
        text +
        'Отправьте ссылку пользователю с которым хотите сыграть.\n' +
        await deep_linking.get_start_link(str(who), encode=True)
    )


@dp.message_handler(commands='restart')
async def starting(message: types.Message):
    game_state.delete_game(message.from_user.id)
    await send_start_message(message.from_user.id, 'Текущая партия сброшена\n')

def make_board_markup(field):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    emojis = {
        'o': '⭕',
        'x': '❌',
        '.': '◽'
    }

    for i in range(0, 3):
        text_and_data = []
        for j in range(0, 3):
            text_and_data.append((emojis[field[i * 3 + j]], f'{j}, {i}'))
        row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
        keyboard_markup.row(*row_btns)

    return keyboard_markup

@dp.callback_query_handler(text='0, 0')
@dp.callback_query_handler(text='0, 1')
@dp.callback_query_handler(text='0, 2')
@dp.callback_query_handler(text='1, 0')
@dp.callback_query_handler(text='1, 1')
@dp.callback_query_handler(text='1, 2')
@dp.callback_query_handler(text='2, 0')
@dp.callback_query_handler(text='2, 1')
@dp.callback_query_handler(text='2, 2')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    game = game_state.find_game(query.from_user.id)
    if game is None:
        await query.answer('Игра окончена')
        return

    if game['last_move'] == query.from_user.id:
        await query.answer('Дождитесь вашего хода!')
        return
        
    (coord_x, coord_y) = query.data.split(',')
    index = int(coord_x) + int(coord_y) * 3
    if game['board'][index] != '.':
        await query.answer('Клетка уже занята!')
        return

    game['board'][index] = 'x' if game['player1'] == query.from_user.id else 'o'
    game['last_move'] = query.from_user.id
    another_player = game['player2'] if game['player1'] == query.from_user.id else game['player1']

    # always answer callback queries, even if you have nothing to say
    markup = make_board_markup(game['board'])
    win = game_state.check_win(game['board'])
    if not win:
        await query.answer()
        await bot.send_message(query.from_user.id, 'Ход соперника:', reply_markup=markup)
        await bot.send_message(another_player, 'Ваш ход:', reply_markup=markup)
        return

    if win == 'draw':
        await bot.send_message(game['player1'], 'Ничья!', reply_markup=markup)
        await bot.send_message(game['player2'], 'Ничья!', reply_markup=markup)
        await send_start_message(
            game['player1'], 
            'Если хотите сыграть ещё раз:\n')
        await send_start_message(
            game['player2'],
            'Если хотите сыграть ещё раз:\n')
        return

    winner = game['player1'] if win == 'x' else game['player2']
    loser = game['player1'] if win == 'o' else game['player2']
    await bot.send_message(winner, 'Вы победили!', reply_markup=markup)
    await bot.send_message(loser, 'Вы проиграли!', reply_markup=markup)
    game_state.delete_game(game['player1'])
    await send_start_message(
        winner, 
        'Поздравляем с победой!\n' +
        'Если хотите сыграть ещё раз:\n')
    await send_start_message(
        loser, 
        'К сожалению, вы проиграли!\n' +
        'Если хотите сыграть ещё раз:\n')
