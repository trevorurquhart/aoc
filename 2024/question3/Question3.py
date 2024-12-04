import re


def solve_two(input):
    delimited = 'do()' + input.replace('\n', '') + 'don\'t()'
    split = re.findall('do\(\).*?don\'t\(\)', delimited)
    return sum([solve_one(x) for x in split])


def solve_one(input):
    search = re.findall('mul\\(([0-9]{1,3}),([0-9]{1,3})\)', input)
    return sum([int(x) * int(y) for x, y in search])


with open('input.txt') as f:
    file = f.read()
    print(solve_one(file))
    print(solve_two(file))
