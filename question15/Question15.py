import re


def solve_one(line_no, sensors, beacons):
    beacon_cnt = sum([1 for x in beacons if x[1] == line_no])
    coords = calc_taken_coords(line_no, sensors)
    taken = sum_ranges(coords)
    print(taken - beacon_cnt)


def sum_ranges(coords):
    coords.sort()
    taken = coords[0][1] - coords[0][0] + 1
    m = coords[0][1]
    for i in range(1, len(coords)):
        current_coord = coords[i]
        taken += max(0, current_coord[1] - m) - max(0, current_coord[0] - m - 1)
        m = max(m, current_coord[1])
    return taken


def calc_taken_coords(line_no, sensors, lower_limit = lambda x: x, upper_limit = lambda x: x):
    token_coords = []
    for s, dist in sensors.items():
        y_dist = abs(s[1] - line_no)
        diff = dist - y_dist
        if diff >= 0:
            x1 = lower_limit(s[0] - diff)
            x2 = upper_limit(s[0] + diff)
            token_coords.append((x1, x2))
    return token_coords


def find_beacon(line_no, sensors, upper):
    taken_coords = calc_taken_coords(line_no, sensors, lambda x: max(x, 0), lambda x: min(upper, x))
    taken_coords.sort()
    max_coord = 0
    for c in taken_coords:
        if c[0] <= max_coord + 1:
            max_coord = max(max_coord, c[1])
        else:
            break

    if max_coord != upper:
        return max_coord + 1, line_no, 4000000 * (max_coord + 1) + line_no

    return None


def solve_two(upper, sensors):
    for y in range(0, upper + 1):
        beacon = find_beacon(y, sensors, upper)
        if beacon is not None:
            print(beacon)
            return


with open('question_data.txt') as q:
    data = [list(map(int, re.findall("-\\d+|\\d+", l.strip()))) for l in q.readlines()]
    sensors = {}
    beacons = set()
    for sb in data:
        sensors[(sb[0], sb[1])] = abs(sb[0] - sb[2]) + abs(sb[1] - sb[3])
        beacons.add((sb[2], sb[3]))

    # solve_one(10, sensors, beacons)
    # solve_two(20, sensors)
    solve_one(2000000, sensors, beacons)
    solve_two(4000000, sensors)
