class TheirMove:
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class MyMove:
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Outcome:
    LOSS = "X"
    DRAW = "Y"
    WIN = "Z"


shape_to_win = {TheirMove.ROCK: MyMove.PAPER, TheirMove.PAPER: MyMove.SCISSORS, TheirMove.SCISSORS: MyMove.ROCK}
to_lose = {TheirMove.ROCK: MyMove.SCISSORS, TheirMove.PAPER: MyMove.ROCK, TheirMove.SCISSORS: MyMove.PAPER}
shape_to_draw = {TheirMove.ROCK: MyMove.ROCK, TheirMove.PAPER: MyMove.PAPER, TheirMove.SCISSORS: MyMove.SCISSORS}


def shape_score(shape):
    return 1 if shape == MyMove.ROCK else (2 if shape == MyMove.PAPER else 3)


def game_score(game_outcome):
    return 6 if game_outcome == Outcome.WIN else (3 if game_outcome == Outcome.DRAW else 0)


def game_result(their_shape, my_shape):
    if my_shape == shape_to_win[their_shape]:
        return Outcome.WIN

    if my_shape == shape_to_draw[their_shape]:
        return Outcome.DRAW

    return Outcome.LOSS


def shape_to_play(their_shape, result):
    if result == Outcome.WIN:
        return shape_to_win[their_shape]
    elif result == Outcome.LOSS:
        return to_lose[their_shape]
    else:
        return shape_to_draw[their_shape]


def solve_one(lines):
    score = 0
    for line in lines:
        their_shape, my_shape = [s for s in line.split(' ')]
        score += shape_score(my_shape) + game_score(game_result(their_shape, my_shape))
    print(score)


def solve_two(lines):
    score = 0
    for line in lines:
        their_shape_code, result_code = line.split(' ')
        score += shape_score(shape_to_play(their_shape_code, result_code)) + game_score(result_code)
    print(score)


with open('question_data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve_one(lines)
    solve_two(lines)
