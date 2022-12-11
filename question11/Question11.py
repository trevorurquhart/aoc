import math


class Monkey:

    def __init__(self, items, op, test, if_true, if_false):
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.no_of_inspections = 0

    def add_item(self, item):
        self.items.append(item)

    def throw(self, item, monkeys):
        target_monkey = self.if_true if item % self.test == 0 else self.if_false
        monkeys[target_monkey].add_item(item)

    def inspect(self, monkeys, worry_fn):
        while self.items:
            self.no_of_inspections += 1
            item = worry_fn(self.op(self.items.pop(0)))
            self.throw(item, monkeys)


def parse_monkeys(lines):
    monkeys = []
    params = []
    for line in lines:
        match line.split():
            case ["Starting", "items:", *items]:
                params.append([int(item.replace(",", "")) for item in items])
            case ["Operation:", "new", "=", "old", "*", m]:
                params.append((lambda x: x * x) if m == "old" else (lambda x, m=m: x * int(m)))
            case ["Operation:", "new", "=", "old", "+", a]:
                params.append((lambda x: x + x) if a == "old" else (lambda x, a=a: x + int(a)))
            case ["Test:", "divisible", "by", s]:
                params.append(int(s))
            case ["If", "true:", "throw", "to", "monkey", true_monkey]:
                params.append(int(true_monkey))
            case ["If", "false:", "throw", "to", "monkey", false_monkey]:
                params.append(int(false_monkey))
                monkeys.append(Monkey(*params))
                params = []
    return monkeys


def solve(monkeys, rounds, worry_fn):
    for r in range(rounds):
        for monkey in monkeys:
            monkey.inspect(monkeys, worry_fn)
    ins = [m.no_of_inspections for m in monkeys]
    ins.sort()
    top, second = ins[-2:]
    print(top * second)


def solve_one(lines):
    solve(parse_monkeys(lines), 20, lambda x: x // 3)


def solve_two(lines):
    monkeys = parse_monkeys(lines)
    lcm = math.lcm(*[m.test for m in monkeys])
    solve(monkeys, 10000, lambda x: x % lcm)


with open('question_data.txt') as q:
    lines = [line.strip() for line in q.readlines()]
    solve_one(lines)
    solve_two(lines)
