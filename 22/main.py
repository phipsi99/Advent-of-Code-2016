from itertools import permutations
from pathlib import Path
import re

from networkx import Graph
import networkx

def get_viable_pairs(nodes, dist = None):
    pairs = permutations(nodes, 2)
    viable_pairs = []
    for nodeA, nodeB in pairs:
        if dist and not (abs(nodeB[0] - nodeA[0]) +  abs(nodeB[1] - nodeA[1])) == dist:
            continue
        sizeA, usedA, availA = nodes[nodeA]
        sizeB, usedB, availB = nodes[nodeB]
        if usedA > 0 and usedA <= availB:
            viable_pairs.append((nodeA, nodeB))
    return viable_pairs

def get_first_distance(nodes, max_x, hole, hole_size):
    graph = Graph()
    for (x, y), (size, used, avail) in nodes.items():
        if used > hole_size:
            continue
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx_, ny_ = x + dx, y + dy
            if (nx_, ny_) in nodes and nodes[nx_, ny_][1] <= hole_size:
                graph.add_edge((x, y), (nx_, ny_))
    return networkx.shortest_path_length(graph, hole, (max_x-1,0))

def build_graph(pairs):
    graph = Graph()
    for nodeA, nodeB in pairs:
        graph.add_edge(nodeA, nodeB)
    return graph

def do_main(debug_mode=False):
    with open(Path('22/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('22/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    nodes = {}
    max_x = 0
    hole = ()
    hole_size = 0

    for line_index, line in enumerate(lines):
        try:
            x, y, size, used, avail = re.match(r".*x(\d+)-y(\d+)\s*(\d+)T\s*(\d+)T\s*(\d+)T\s*\d+%", line).groups()
            x, y, size, used, avail = (int(a) for a in (x, y, size, used, avail))
            max_x = max(max_x, x)
            if used == 0:
                hole = (x, y)
                hole_size = avail
            if y in [0,1] and used > 85:
                print("care " + used)
            nodes[(x, y)] = (size, used, avail)
        except:
            continue
    print(len(get_viable_pairs(nodes)))

    first_dist = get_first_distance(nodes, max_x, hole, hole_size)
    distance = first_dist
    for i in range(max_x-1):
        distance += 5
    distance += 1

    print(distance)


if __name__ == '__main__':
    do_main(False)