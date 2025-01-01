from collections import deque
from hashlib import md5
from pathlib import Path

import numpy as np

def bfs(maze, initial_passcode):
    start = (2,2)
    vault = (8,8)

    directions = [(0,-2, "U"),(0,2,"D"), (-2,0,"L"),(2,0,"R")]

    queue = deque([([start], initial_passcode)])
    while queue:
        path, current_passcode = queue.popleft()
        if path[-1] == vault:
            return current_passcode[len(initial_passcode):]
        dirs = []
        current_hash = md5(current_passcode.encode()).hexdigest()
        for i in range(4):
            if current_hash[i] in ["b", "c", "d", "e", "f"]:
                dirs.append(directions[i])
        for dir in dirs:
            new_pos = (path[-1][0] + dir[0], path[-1][1] + dir[1])
            if maze[new_pos] != "#":
                queue.append((path + [new_pos], current_passcode + dir[2]))
    return 0

def bfs2(maze, initial_passcode):
    start = (2,2)
    vault = (8,8)

    directions = [(0,-2, "U"),(0,2,"D"), (-2,0,"L"),(2,0,"R")]
    longest = 0

    queue = deque([([start], initial_passcode)])
    while queue:
        path, current_passcode = queue.popleft()
        if path[-1] == vault:
            longest = max(longest, len(path))-1
            continue
        dirs = []
        current_hash = md5(current_passcode.encode()).hexdigest()
        for i in range(4):
            if current_hash[i] in ["b", "c", "d", "e", "f"]:
                dirs.append(directions[i])
        for dir in dirs:
            new_pos = (path[-1][0] + dir[0], path[-1][1] + dir[1])
            if maze[new_pos] != "#":
                queue.append((path + [new_pos], current_passcode + dir[2]))
    return longest

        

def do_main(debug_mode=False):
    with open(Path('17/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('17/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    maze = np.asanyarray([list(l) for l in lines], str)

    print(bfs(maze, "awrkjxxr"))
    print(bfs2(maze, "awrkjxxr"))
    #print(bfs(maze, "hijkl"))

if __name__ == '__main__':
    do_main(False)