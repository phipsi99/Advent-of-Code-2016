import itertools
from pathlib import Path

import networkx
from tqdm import tqdm

def do_main(debug_mode=False):
    with open(Path('24/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('24/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    graph = networkx.Graph()
    required = []
    start = ()

    for line_index, line in enumerate(lines):
        for col_index, val in enumerate(line):
            if val == "#":
                graph.add_node((col_index, line_index))
            else:
                if val.isdigit():
                    if val == "0":
                        start = (col_index, line_index)
                    else:
                        required.append((col_index, line_index))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = col_index + dx
                    ny = line_index + dy
                    if 0 < nx < len(line) and 0 < ny < len(lines) and lines[ny][nx] != '#':
                        graph.add_edge((col_index, line_index), (nx, ny))

    best_cost = float("inf")
    best_cost_with_return = float("inf")
    required_with_start = required[:]
    required_with_start.append(start)
    combination_pairs = list(itertools.permutations(required_with_start, 2))
    cache = {}
    for curr, next in tqdm(combination_pairs):
        if (next, curr) in cache:
            cache[(curr, next)] = cache[(next, curr)]
            continue
        cache[(curr, next)] = networkx.shortest_path_length(graph, curr, next)

    combinations = list(itertools.permutations(required))
    for perm in tqdm(combinations):
        cost = 0
        current = start

        for nxt in perm:
            segment_cost = cache[(current, nxt)]

            cost += segment_cost
            current = nxt

        cost_with_return = cost + cache[perm[-1], start]
        best_cost = min(best_cost, cost)
        best_cost_with_return = min(best_cost_with_return, cost_with_return)

    print(best_cost)
    print(best_cost_with_return)


if __name__ == '__main__':
    do_main(False)