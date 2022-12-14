def register_value_at_start_of_cycle(lines):
    result = []
    x = 1
    for line in lines:
        match line.split():
            case ["addx", arg]:
                result.append(x)
                result.append(x)
                x = x + int(arg)
            case ["noop"]:
                result.append(x)
    return result


def solve1(result):
    print(sum([(i + 1) * result[i] for i in range(19, len(result), 40)]))


def solve2(result):
    crt = ""
    for cycle in range(240):
        posn = cycle % 40
        if posn == 0 and cycle > 0:
            crt += "\n"

        crt += "# " if result[cycle] - 1 <= posn <= result[cycle] + 1 else ". "

    print(crt)


with open('quesiton_data.txt') as q:
    lines = [cmd.strip() for cmd in q.readlines()]
    result = register_value_at_start_of_cycle(lines)

    solve1(result)
    solve2(result)
