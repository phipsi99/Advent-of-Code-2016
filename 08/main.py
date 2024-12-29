from pathlib import Path
import re
from time import sleep

import numpy as np

def do_main(debug_mode=False):
    with open(Path('08/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('08/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    size = (6, 50)
    #size = (3, 7)
    grid = np.zeros(size, int)

    for line_index, line in enumerate(lines):
        if "rect" in line:
            for coli in range(int(line.split(" ")[1].split("x")[0])):
                for rowi in range(int(line.split(" ")[1].split("x")[1])):
                    grid[rowi, coli] = 1
        elif "rotate row" in line:
            row = int(re.findall(r"\d+", line.split(" ")[2])[0])
            shift = int(line.split(" ")[-1])
            new_row = np.zeros(len(grid[0]), int)
            for i, r in enumerate(grid[row]):
                new_row[(i+shift)%(len(new_row))] = r
            grid[row] = new_row
        elif "rotate column" in line:
            cols = list(zip(*grid))
            col = int(re.findall(r"\d+", line.split(" ")[2])[0])
            shift = int(line.split(" ")[-1])
            new_col = np.zeros(len(grid), int)
            for i, r in enumerate(cols[col]):
                new_col[(i+shift)%(len(new_col))] = r
            grid[:, col] = new_col
        print(chr(27) + "[2J")
        for r in grid:
            print("".join(["█" if x == 1 else " " for x in r]))
        sleep(0.05)

    print(np.count_nonzero(grid))

if __name__ == '__main__':
    do_main(False)