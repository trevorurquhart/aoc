def their_shape(code):
    return "ABC".index(code) + 1


def my_shape(code):
    return "XYZ".index(code) + 1


def game_score(game_outcome):
    return 6 if game_outcome == "Z" else 3 if game_outcome == "Y" else 0


def win(their_shape):
    return 1 if their_shape == 3 else their_shape + 1


def lose(their_shape):
    return 3 if their_shape == 1 else their_shape - 1


def game_result(their_shape, my_shape):
    if my_shape == win(their_shape):
        return 6

    if my_shape == their_shape:
        return 3

    return 0


def shape_score(their_shape, result):
    match result:
        case "Z":
            return win(their_shape)
        case "X":
            return lose(their_shape)
        case _:
            return their_shape


def solve_one(lines):
    score = 0
    for line in lines:
        them, me = line.split(' ')
        score += my_shape(me) + game_result(their_shape(them), my_shape(me))
    print(score)


def solve_two(lines):
    score = 0
    for line in lines:
        them, result = line.split(' ')
        score += shape_score(their_shape(them), result) + game_score(result)
    print(score)


with open('question_data.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve_one(lines)
    solve_two(lines)
