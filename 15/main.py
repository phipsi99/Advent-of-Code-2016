from collections import deque
from pathlib import Path
import re

def bfs(discs):
    queue = deque([(0, 0)])
    while queue:
        passed_discs_idx, time = queue.popleft()
        if len(discs) == passed_discs_idx:
            return time - len(discs)
        time += 1
        total_pos, init_pos = discs[passed_discs_idx]
        if (init_pos+time) % total_pos == 0:
            queue.append((passed_discs_idx+1, time))
        if passed_discs_idx == 0:
            queue.append((passed_discs_idx, time))
        
        

def do_main(debug_mode=False):
    with open(Path('15/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('15/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    discs = []

    for line_index, line in enumerate(lines):
        _, total_pos, _, init_pos = re.findall(r"\d+", line)
        discs.append((int(total_pos), int(init_pos)))
    
    print(bfs(discs))

if __name__ == '__main__':
    do_main(False)