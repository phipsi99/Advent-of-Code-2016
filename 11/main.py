from collections import deque
from pathlib import Path

init_state = [["HM", "LM"],["HG", "LM", "HM"],["LG"],[]] 

def is_safe(state):
    for floor in state:
        generators = [g for g in floor if "G" in g]
        microchips = [g for g in floor if "M" in g]
        for mc in microchips:
            for gen in generators:
                if mc[0] != gen[0]:
                    if not any(g[0] == mc[0] for g in generators):
                        return False
    return True

def bfs(initial_state):
    queue = deque([(initial_state, 0, 0)])
    elevator = 0
    total_len = sum([len(f) for f in initial_state])

    while queue:
        state, elevator, step_count = queue.popleft()
        if not is_safe(state):
            continue
        if len(state[3] == total_len):
            return step_count
        for elem in state[elevator]:
            # possibilities each one and combinations each up and down


def do_main(debug_mode=False):
    with open(Path('11/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('11/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    print(is_safe(init_state))

    for line_index, line in enumerate(lines):
        r = [int(i) for i in line.split(" ")]

if __name__ == '__main__':
    do_main(False)