def transpose(matrix):
    m = [[] for i in range(len(matrix[0]))]
    for row in matrix:
        for idx, t in enumerate(row):
            m[idx].append(t)
    return m


def reverse(matrix):
    return [list(r) for r in list((map(reversed, matrix)))]


def merge(array1, array2, fn):
    for idx1, e1 in enumerate(array1):
        for idx2, e2 in enumerate(e1):
            array1[idx1][idx2] = fn(e2, array2[idx1][idx2])
    return array1


def find_visible(rows):
    return [is_visible(row) for row in rows]


def find_views(rows):
    return [can_view(row) for row in rows]


def is_visible(row):
    max_height = -1
    visible = []
    for t in row:
        visible.append(1 if t > max_height else 0)
        max_height = max(t, max_height)
    return visible


def can_view(row):
    view = []
    for idx, c in enumerate(row):
        cnt = 0
        for t in row[idx + 1:]:
            cnt += 1
            if t >= c:
                break
        view.append(cnt)
    return view


def solve(rows, fn, fn2, fn3):
    ans = fn(rows)
    ans = merge(ans, transpose(fn(transpose(rows))), fn2)
    ans = merge(ans, reverse(fn(reverse(rows))), fn2)
    ans = merge(ans, transpose(reverse(fn(reverse(transpose(rows))))), fn2)

    print(fn3([fn3(i) for i in ans]))


with open('question_data.txt') as q:
    data = [list(map(int, l)) for l in [list(line.strip()) for line in q.readlines()]]
    solve(data, find_visible, max, sum)
    solve(data, find_views, lambda x, y: x * y, max)
