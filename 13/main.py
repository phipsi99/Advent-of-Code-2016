from collections import deque
from pathlib import Path

import numpy as np

def create_maze(size, favourite_number):
    maze = np.full((size, size), ".", str)
    for x in range(size):
        for y in range(size):
            v = x*x + 3*x + 2*x*y + y + y*y
            v += favourite_number
            if bin(v).count("1") % 2 != 0:
                maze[x,y] = "#"
    return maze

def solve_maze(maze, target):
    queue = deque([((1,1), 0, [(1,1)])])
    visited = set()
    visited.add((1,1))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        pos, steps, path = queue.popleft()
        if pos == target:
            return steps, path
        for dir in directions:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if 0 < new_pos[0] < len(maze[0]) and 0 < new_pos[1] < len(maze[0]) and new_pos not in visited:
                if maze[new_pos] != "#":
                    visited.add(new_pos)
                    queue.append((new_pos, steps + 1, path + [new_pos]))
    return 0, 0

def count_locations(maze):
    queue = deque([((1,1), 0, [(1,1)])])
    visited = set()
    visited.add((1,1))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        pos, steps, path = queue.popleft()
        if steps == 50:
            continue
        for dir in directions:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if 0 <= new_pos[0] < len(maze[0]) and 0 <= new_pos[1] < len(maze[0]) and new_pos not in path:
                if maze[new_pos] != "#":
                    visited.add(new_pos)
                    queue.append((new_pos, steps + 1, path + [new_pos]))
    for vis in visited:
        maze[vis] = 'O'
    
    return len(visited)

def do_main(debug_mode=False):
    fav = 1362
    target = (31, 39)
    
    if debug_mode:
        fav = 10
        target = (7,4)

    point_sum = 0

    maze = create_maze(1000, fav)
    print(solve_maze(maze, target))
    print(count_locations(maze))

if __name__ == '__main__':
    do_main(False)