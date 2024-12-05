class Page:

    def __init__(self, value):
        self.value = value
        self.pages_before = set()

    def before(self, page):
        self.pages_before.add(page.value)

    def is_before(self, v):
        return v in self.pages_before


def sort(page_numbers, pages):
    result = []
    for p in page_numbers:
        ins = next((idx for idx, v in enumerate(result) if pages.get(p).is_before(v)), len(result))
        result.insert(ins, p)
    return result


def parse(rules):
    pages = {}
    for before, after in rules:
        before_page = pages.setdefault(before, Page(before))
        after_page = pages.setdefault(after, Page(after))
        before_page.before(after_page)
    return pages


def count_valid(page_numbers, pages):
    for idx, p in enumerate(page_numbers):
        if any(pages.get(p).is_before(e) for e in page_numbers[:idx]):
            return 0
    return page_numbers[len(page_numbers)//2]


def count_in_valid(page_numbers, pages):
    for idx, p in enumerate(page_numbers):
        if any(pages.get(p).is_before(e) for e in page_numbers[:idx]):
            fix_order = sort(page_numbers, pages)
            return fix_order[len(fix_order) // 2]
    return 0


def solve_one(pages, page_numbers):
    print(sum([count_valid(pn, pages) for pn in page_numbers]))


def solve_two(pages, page_numbers):
    print(sum([count_in_valid(pn, pages) for pn in page_numbers]))


with open('input_order.txt') as o:
    with open('input_updates.txt') as u:
        rules = [r.strip() for r in o.readlines()]
        updates = [u.strip() for u in u.readlines()]
        pages = parse([(int(x), int(y)) for x, y in [r.split('|') for r in rules]])
        page_numbers = [[int(p) for p in upd.split(',')] for upd in updates]
        solve_one(pages, page_numbers)
        solve_two(pages, page_numbers)
