from pathlib import Path

import numpy as np

def do_main(debug_mode=False):
    with open(Path('20/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('20/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    blocked_ips = np.zeros(3384842620)

    for line_index, line in enumerate(lines):
        start,end = [int(i) for i in line.split("-")]
        blocked_ips[start:end] = 1
    print(np.where(blocked_ips == 0)[0])


if __name__ == '__main__':
    do_main(True)