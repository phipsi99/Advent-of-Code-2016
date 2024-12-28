from pathlib import Path
import re

def do_main(debug_mode=False):
    with open(Path('07/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('07/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        abbas_inside = re.findall(r"\[[a-z]*([a-z])([a-z])\2\1[a-z]*]", line)
        for abba in abbas_inside:
            if all(abba[0] == a for a in abba):
                continue
        abbas = re.findall(r"([a-z])([a-z])\2\1", line)
        for abba in abbas:
            if not all(abba[0] == a for a in abba):
                point_sum += 1
                continue

    print(point_sum)
        

if __name__ == '__main__':
    do_main(False)