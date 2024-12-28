# 16:25 min
from collections import Counter
from pathlib import Path

def do_main(debug_mode=False):
    with open(Path('06/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('06/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    grid = []


    for line_index, line in enumerate(lines):
        grid.append([])
        for c in line:
            grid[line_index].append(c)

    cols = zip(*grid)

    counters = []
    for c in cols:
        counters.append(Counter(c))
    
    s = ""
    for counter in counters:
        s+=str(counter.most_common()[0][0][0])
    print(s)

    s2 = ""
    for counter in counters:
        s2+=str(counter.most_common()[-1][0][0])
    print(s2)

if __name__ == '__main__':
    do_main()