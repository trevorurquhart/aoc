import math


def do_op(p, op_code, operand, reg, out):
    combo = combos(operand, reg)
    # print(f'{op_code} ({operand}, {combo})')
    match op_code:
        case 0:
            reg['A'] = int(reg['A'] // math.pow(2, combo))
        case 1:
            reg['B'] = reg['B'] ^ operand
        case 2:
            reg['B'] = combo % 8
        case 3:
            if reg['A'] != 0:
                return operand
        case 4:
            reg['B'] = reg['B'] ^ reg['C']
        case 5:
            out.append(combo % 8)
        case 6:
            reg['B'] = int(reg['A'] // math.pow(2, combo))
        case 7:
            reg['C'] = int(reg['A'] // math.pow(2, combo))

    return p + 2


def combos(literal, reg):
    match literal:
        case _ if 0 <= literal <= 3:
            return literal
        case 4:
            return reg['A']
        case 5:
            return reg['B']
        case 6:
            return reg['C']
        case _:
            return None


def run_program(prog, reg, check_for_p = False):
    p = 0
    out = []
    while p < len(prog):
        p = do_op(p, prog[p], prog[p + 1], reg, out)
        if check_for_p:
            if prog[:len(out)] != out:
                break
    return out


def find_next_possible(ans, prog, desired_out):
    poss = []
    shifted = ans << 3
    for A in range(0, 7):
        a = shifted + A
        reg = {'A': a, 'B': 0, 'C': 0}
        out = run_program(prog, reg)
        if desired_out == out:
            poss.append(a)
    return poss


def solve_two(prog):
    print(prog)
    answers = [0]
    for n in range(1, len(prog) + 1):
        desired = prog[-n:]
        for x in range(len(answers)):
            ans = answers.pop(0)
            for p in find_next_possible(ans, prog, desired):
                if desired == prog:
                    return p
                answers.append(p)


with open("input.txt") as f:
    # run_program([2, 6], {'A': 0, 'B': 0, 'C': 9})
    # run_program([5, 0, 5, 1, 5, 4], {'A': 10, 'B': 0, 'C': 0})
    # run_program([0, 1, 5, 4, 3, 0], {'A': 2024, 'B': 0, 'C': 0})
    # run_program([1,7], {'A': 0, 'B': 29, 'C': 0})
    # run_program([4, 0], {'A': 0, 'B': 2024, 'C': 43690})
    program = [int(p) for p in f.read().strip().split(",")]
    print(run_program(program, {'A': 100611, 'B': 0, 'C': 0}))
    two_ans = solve_two(program)
    print(run_program(program, {'A': two_ans, 'B': 0, 'C': 0}))
    print(two_ans)