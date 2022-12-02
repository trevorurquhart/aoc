from PaperScissorsStone import shape_to_win
from PaperScissorsStone import ROCK
from PaperScissorsStone import PAPER
from PaperScissorsStone import SCISSORS


def shape(code):
    return ROCK if code in ("A", "X") else (PAPER if code in ("B", "Y") else SCISSORS)


def shape_score(shape):
    return 1 if shape == ROCK else (2 if shape == PAPER else 3)


def game_score(theirShape, myShape):
    if myShape == shape_to_win(theirShape):
        return 6

    if myShape == theirShape:
        return 3

    return 0


with open('question_data.txt') as f:
    score = 0
    for line in f:
        theirShape, myShape = [shape(s.strip()) for s in line.split(' ')]
        score += shape_score(myShape) + game_score(theirShape, myShape)

    print(score)
