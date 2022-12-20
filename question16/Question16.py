import re
import operator


class Valve:

    def __init__(self, name, flow_rate, neighbours):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = neighbours


def bfs(start, candidates, valves):
    dist = {}
    queue = [(start, 0)]
    visited = [start]
    while queue:
        valve, dist = queue.pop(0)
        if (start, valve) not in dist and valve in candidates:
            dist[(start, valve)] = dist

        if len(dist) == len(candidates):
            break

        for n in valves[valve].neighbours:
            if n not in visited:
                queue.append((n, dist + 1))
                visited.append(n)

    return dist


def find_distances(candidate_valves, valves):
    distances = {}
    for v in candidate_valves:
        distances = distances | bfs(v, candidate_valves, valves)

    return distances


def find_paths(valves, dist, available_time):
    dest_valves = [v for v in valves.values() if v.flow_rate > 0]
    queue = [("AA", available_time, 0, set())]
    max_paths = {}
    while queue:
        valve, time_remaining, total_relief, valves_opened = queue.pop(0)

        for cv in [v for v in dest_valves if v.name not in valves_opened]:
            dist_to_valve = dist[valve, cv.name]
            if dist_to_valve < time_remaining - 1:
                time = time_remaining - dist_to_valve - 1
                relief = total_relief + cv.flow_rate * time
                opened = set(valves_opened)
                opened.add(cv.name)
                key = frozenset(opened)
                if key in max_paths:
                    max_paths[key] = max(max_paths[key], relief)
                else:
                    max_paths[key] = relief
                queue.append((cv.name, time, relief, opened))

    return max_paths


def solve_one(valves, distances):
    max_paths = find_paths(valves, distances, 30)
    ans = max(max_paths.items(), key=operator.itemgetter(1))
    print(ans[0], ans[1])


def solve_two(valves, distances):
    max_paths = find_paths(valves, distances, 26)
    max_relief = 0
    ans = None
    for path1, relief1 in max_paths.items():
        for path2, relief2 in max_paths.items():
            if set.isdisjoint(set(path1), set(path2)):
                relief = relief1 + relief2
                if relief > max_relief:
                    max_relief = relief
                    ans = (path1, path2, relief)

    print(ans)


with open('question_data.txt') as q:
    data = [re.findall('[A-Z]{2}|\\d+', l.strip()) for l in q.readlines()]
    valves = {v.name: v for v in [Valve(x[0], int(x[1]), x[2:]) for x in data]}
    candidate_valves = [v.name for v in valves.values() if v.flow_rate > 0]
    distances = find_distances(["AA"] + candidate_valves, valves)

    solve_one(valves, distances)
    solve_two(valves, distances)
