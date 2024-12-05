from collections import defaultdict


def sort(pg_nums, pages):
    result = []
    for p in pg_nums:
        ins = next((idx for idx, v in enumerate(result) if v in pages.get(p)), len(result))
        result.insert(ins, p)
    return result


def parse(rules):
    pages = defaultdict(list)
    for before, after in rules:
        pages[before].append(after)
    return pages


def count_valid(pg_nums, pages):
    for idx, p in enumerate(pg_nums):
        if any(e in pages.get(p) for e in pg_nums[:idx]):
            return 0
    return pg_nums[len(pg_nums) // 2]


def count_invalid(pg_nums, pages):
    for idx, p in enumerate(pg_nums):
        if any(e in pages.get(p) for e in pg_nums[:idx]):
            ordered = sort(pg_nums, pages)
            return ordered[len(ordered) // 2]
    return 0


def solve_one(pages, page_numbers):
    print(sum([count_valid(pn, pages) for pn in page_numbers]))


def solve_two(pages, page_numbers):
    print(sum([count_invalid(pn, pages) for pn in page_numbers]))


with open('input_order.txt') as o:
    with open('input_updates.txt') as u:
        pages = parse([(int(x), int(y)) for x, y in [r.strip().split('|') for r in o.readlines()]])
        page_numbers = [[int(p) for p in upd.split(',')] for upd in [u.strip() for u in u.readlines()]]
        solve_one(pages, page_numbers)
        solve_two(pages, page_numbers)
