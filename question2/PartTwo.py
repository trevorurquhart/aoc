from PaperScissorsStone import PAPER
from PaperScissorsStone import ROCK
from PaperScissorsStone import shape_to_lose
from PaperScissorsStone import shape_to_win

LOSS = "X"
DRAW = "Y"
WIN = "Z"


def game_score(game_outcome):
    return 6 if game_outcome == WIN else (3 if game_outcome == DRAW else 0)


def shape_score(their_shape, result):
    if result == WIN:
        my_shape = shape_to_win(their_shape)
    elif result == LOSS:
        my_shape = shape_to_lose(their_shape)
    else:
        my_shape = their_shape

    return 1 if my_shape == ROCK else (2 if my_shape == PAPER else 3)


with open('question_data.txt') as f:
    total = 0
    for line in f:
        their_shape_code, result_code = [s.strip() for s in line.split(' ')]
        total += shape_score(their_shape_code, result_code) + game_score(result_code)

    print(total)
