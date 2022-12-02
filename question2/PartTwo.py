from PaperScissorsStone import PAPER
from PaperScissorsStone import ROCK
from PaperScissorsStone import shape_to_lose
from PaperScissorsStone import shape_to_win

LOSS = "X"
DRAW = "Y"
WIN = "Z"

def game_score(game_outcome):
    return 6 if game_outcome == WIN else (3 if game_outcome == DRAW else 0)


def shape_to_play_score(their_shape, result):
    if result == WIN:
        shape_to_play = shape_to_win(their_shape)
    elif result == LOSS:
        shape_to_play = shape_to_lose(their_shape)
    else:
        shape_to_play = their_shape

    return 1 if shape_to_play == ROCK else (2 if shape_to_play == PAPER else 3)


with open('question_data.txt') as f:
    total = 0
    for line in f:
        their_shape_code, result_code = [s.strip() for s in line.split(' ')]
        total += shape_to_play_score(their_shape_code, result_code) + game_score(result_code)

    print(total)
