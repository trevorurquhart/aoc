SCISSORS = "C"
PAPER = "B"
ROCK = "A"

WIN_MAP = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}
LOSE_MAP = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}


def shape_to_win(opponent_move):
    return WIN_MAP[opponent_move]


def shape_to_lose(opponent_move):
    return LOSE_MAP[opponent_move]
