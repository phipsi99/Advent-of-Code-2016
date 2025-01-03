from pathlib import Path
from tqdm import tqdm

import numpy as np

def do_main(debug_mode=False):
    with open(Path('20/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('20/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    ranges = []


    for line_index, line in enumerate(lines):
        start,end = [int(i) for i in line.split("-")]
        ranges.append((start, end))
    ranges.sort()

    new_ranges = []
    for start, end in ranges:
        if not new_ranges or new_ranges[-1][1] < start - 1:
            new_ranges.append((start, end))
        else:
            new_ranges[-1] = (new_ranges[-1][0], max(new_ranges[-1][1], end))
                
    all_open = []
    for index in tqdm(range(len(new_ranges)-1)):
        all_open += list(range(new_ranges[index][1]+1, new_ranges[index+1][0]))
    print(len(all_open) + 4294967295-new_ranges[-1][1] + new_ranges[0][0])

if __name__ == '__main__':
    do_main(False)