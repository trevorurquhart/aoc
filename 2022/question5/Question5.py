import re


def find_move(line):
    return list(map(int, re.findall('\\d+', line)))


def parse_crates(lines):
    stacks = []
    for line in lines:
        stack_number = 0
        for i in range(1, len(line), 4):
            if len(stacks) < stack_number + 1:
                stacks.append([])
            if line[i] != " ":
                stacks[stack_number].insert(0, line[i])
            stack_number = stack_number + 1
    return stacks


def solveOne(crate_lines, moves, move_as_one=False):
    crates = parse_crates(crate_lines)
    for line in moves:
        m, f, t = find_move(line)
        to_move = crates[f - 1][-m:]
        to_move = list(to_move if move_as_one else reversed(to_move))
        crates[t - 1].extend(to_move)
        del crates[f - 1][-m:]

    print("".join([item[-1:][0] if len(item) > 0 else '' for item in crates]))


with open('question_data.txt') as f:
    lines = [line for line in f.readlines()]
    crates = [line.replace('\n', '') for line in lines if not line.startswith("move")]
    moves = [line.strip() for line in lines if line.startswith("move")]
    # solveOne(crates, moves)
    # solveOne(crates, moves, True)
