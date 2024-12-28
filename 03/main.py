# 11:47 min

from pathlib import Path
import re

def do_main(debug_mode=False):
    with open(Path('03/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('03/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    triangles = []

    for line_index, line in enumerate(lines):
        triangles.append([int(side) for side in re.findall(r'\d+', line)])

    for triangle in triangles:
        t = triangle
        max_side = max(t)
        t.remove(max_side)
        if sum(t) > max_side:
            point_sum += 1
    print(point_sum)

    triangles = [[],[],[]]
    total_index  = 0
    cnt = 0
    for line_index, line in enumerate(lines):
        for index, side in enumerate(re.findall(r'\d+', line)):
            triangles[index + total_index].append(int(side))
        cnt += 1
        if cnt % 3 == 0:
            triangles.append([])
            triangles.append([])
            triangles.append([])
            total_index += 3
            cnt = 0

    point_sum2 = 0
    for triangle in triangles:
        if len(triangle) == 0:
            continue
        t = triangle
        max_side = max(t)
        t.remove(max_side)
        if sum(t) > max_side:
            point_sum2 += 1
    print(point_sum2)

if __name__ == '__main__':
    do_main(False)