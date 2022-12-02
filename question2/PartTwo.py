LOSS = "Loss"
DRAW = "Draw"
WIN = "Win"
SCISSORS = "Scissors"
PAPER = "Paper"
ROCK = "Rock"


def shape(code):
    return ROCK if code == "A" else (PAPER if code == "B" else SCISSORS)


def outcome(code):
    return WIN if code == "Z" else (DRAW if code == "Y" else LOSS)


def game_score(code):
    game_outcome = outcome(code)
    return 6 if game_outcome == WIN else (3 if game_outcome == DRAW else 0)


def shape_to_play_score(their_shape_code, result_code):
    game_outcome = outcome(result_code)
    their_shape = shape(their_shape_code)

    shape_to_play = their_shape
    if game_outcome == WIN:
        shape_to_play = ROCK if their_shape == SCISSORS else (PAPER if their_shape == ROCK else SCISSORS)

    if game_outcome == "Loss":
        shape_to_play = ROCK if their_shape == PAPER else (PAPER if their_shape == SCISSORS else SCISSORS)

    return 1 if shape_to_play == ROCK else (2 if shape_to_play == PAPER else 3)


with open('question_data.txt') as f:
    total = 0
    for line in f:
        their_shape_code, result_code = [s.strip() for s in line.split(' ')]
        total += shape_to_play_score(their_shape_code, result_code) + game_score(result_code)

    print(total)
