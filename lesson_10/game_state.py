games = []

def add_game(player1, player2):
    game = { 'player1': player1, 'player2': player2, 'last_move': player2, 'board': ['.' for _ in range(0, 9)] }
    games.append(game)
    return game

def find_game(player):
    found = list(filter(lambda game: game['player1'] == player or game['player2'] == player, games))
    if len(found) > 0:
        return found[0]
    return None

def delete_game(player):
    game = find_game(player)
    if game in games:
        games.pop(games.index(game))
    
    
def check_win(field):
    for i in range(0, 3):
        if field[i*3] == field[i*3+1] == field[i*3+2] != '.':
            return field[i*3]

    for i in range(0, 3):
        if field[i] == field[i+3] == field[i+6] != '.':
            return field[i]

    for i in range(0, 2):
        if field[2*i] == field[4] == field[8-2*i] != '.':
            return field[2*i]

    if len([_ for _ in field if _ == '.']) == 0:
        return 'draw'

    return False