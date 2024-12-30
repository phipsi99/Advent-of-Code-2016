from collections import deque
import copy
from itertools import combinations
from pathlib import Path

init_state_test = [["HM", "LM"],["HG"],["LG"],[]] 

init_state_real = [["PG", "PM"],["CG", "KG", "RG", "AG"],["CM", "KM", "RM", "AM"],[]] 
init_state_real2 = [["PG", "PM", "EG", "EM", "DG", "DM"],["CG", "KG", "RG", "AG"],["CM", "KM", "RM", "AM"],[]] 

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
    visited = set()
    hashable = tuple([tuple(sorted(l)) for l in initial_state])
    visited.add((hashable, elevator))
    while queue:
        state, elevator, step_count = queue.popleft()
        if not is_safe(state):
            continue
        if len(state[3]) == total_len:
            return step_count
        all_elements = state[elevator]
        combs_of_2 = combinations(all_elements, 2)
        valid_combs_of_2 = []
        for comb in combs_of_2:
            if is_safe([comb]):
                valid_combs_of_2.append(comb)
        for element in all_elements:
            if elevator < 3:
                new_state = copy.deepcopy(state)
                new_state[elevator].remove(element)
                new_state[elevator+1].append(element)
                hashable = tuple([tuple(sorted(l)) for l in new_state])
                if is_safe(new_state) and (hashable, elevator+1) not in visited:
                    visited.add((hashable, elevator+ 1))
                    queue.append((new_state, elevator + 1, step_count+1))
            if elevator > 0:
                new_state = copy.deepcopy(state)
                new_state[elevator].remove(element)
                new_state[elevator-1].append(element)
                hashable = tuple([tuple(sorted(l)) for l in new_state])
                if is_safe(new_state) and (hashable, elevator-1) not in visited:
                    visited.add((hashable, elevator- 1))
                    queue.append((new_state, elevator - 1, step_count+1))
        for comb in valid_combs_of_2:
            if elevator < 3:
                new_state = copy.deepcopy(state)
                for element in comb:
                    new_state[elevator].remove(element)
                    new_state[elevator+1].append(element)
                hashable = tuple([tuple(sorted(l)) for l in new_state])
                if is_safe(new_state) and (hashable, elevator+1) not in visited:
                    visited.add((hashable, elevator+ 1))
                    queue.append((new_state, elevator + 1, step_count+1))
            if elevator > 0:
                new_state = copy.deepcopy(state)
                for element in comb:
                    new_state[elevator].remove(element)
                    new_state[elevator-1].append(element)
                hashable = tuple([tuple(sorted(l)) for l in new_state])
                if is_safe(new_state) and (hashable, elevator-1) not in visited:
                    visited.add((hashable, elevator- 1))
                    queue.append((new_state, elevator - 1, step_count+1))
    return 0

def do_main(debug_mode=False):
    with open(Path('11/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('11/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    print(bfs(init_state_real2))
    print(bfs(init_state_real))

if __name__ == '__main__':
    do_main(False)