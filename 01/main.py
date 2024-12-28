# 17:10 min

from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('01/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('01/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    #dirs = {"north":(0, -1), "east": (1, 0), "south":(0, 1), "west": (-1, 0)}
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    

    d = lines[0].split(', ')
    dd = [(s[0], int(s[1:])) for s in d]

    curr_dir_index = 0
    visited = set()
    first_visited = None
    pos = (0, 0)
    visited.add(pos)
    for dir, dist in dd:
        if dir == 'R':
            curr_dir_index += 1
            if curr_dir_index > 3:
                curr_dir_index = 0
        else:
            curr_dir_index -= 1
            if curr_dir_index < 0:
                curr_dir_index = 3
        curr_dir = dirs[curr_dir_index]
        for i in range(1, dist+1):
            pos2 = (pos[0] + curr_dir[0]*i, pos[1] + curr_dir[1]*i)
            if first_visited is None and pos2 in visited:
                first_visited = pos2
            visited.add(pos2)
        
        pos = (pos[0] + curr_dir[0]*dist, pos[1] + curr_dir[1]*dist)
    
    dist = abs(pos[0]) + abs(pos[1])
    print(dist)

    dist2 = abs(first_visited[0]) + abs(first_visited[1])
    print(dist2)

if __name__ == '__main__':
    do_main(False)