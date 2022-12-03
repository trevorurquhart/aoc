ROCK = "A"
PAPER = "B"
SCISSORS = "C"

LOSS = "X"
DRAW = "Y"
WIN = "Z"

WIN_MAP = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}
LOSE_MAP = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}


def shape_to_win(opponent_move):
    return WIN_MAP[opponent_move]


def shape_to_lose(opponent_move):
    return LOSE_MAP[opponent_move]


def shape_score(shape):
    return 1 if shape == ROCK else (2 if shape == PAPER else 3)


def game_score(game_outcome):
    return 6 if game_outcome == WIN else (3 if game_outcome == DRAW else 0)


def game_result(their_shape, my_shape):
    if my_shape == shape_to_win(their_shape):
        return WIN

    if my_shape == their_shape:
        return DRAW

    return LOSS


def shape_to_play(their_shape, result):
    if result == WIN:
        return shape_to_win(their_shape)
    elif result == LOSS:
        return shape_to_lose(their_shape)
    else:
        return their_shape


def shape(code):
    return ROCK if code in ("A", "X") else (PAPER if code in ("B", "Y") else SCISSORS)


def solve_one(lines):
    score = 0
    for line in lines:
        their_shape, my_shape = [shape(s) for s in line.split(' ')]
        score += shape_score(my_shape) + game_score(game_result(their_shape, my_shape))
    print(score)


def solve_two(lines):
    total = 0
    for line in lines:
        their_shape_code, result_code = line.split(' ')
        total += shape_score(shape_to_play(their_shape_code, result_code)) + game_score(result_code)

    print(total)


with open('question_data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve_one(lines)
    solve_two(lines)
