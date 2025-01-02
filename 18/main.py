import functools
from pathlib import Path

import numpy as np
import tqdm

@functools.cache
def get_new_row(tiles):
    tiles = np.asanyarray(tiles, bool)
    result = np.full(len(tiles), False)
    for tile_idx in range(len(tiles)):
        center = tiles[tile_idx]
        if tile_idx == 0:
            left = False
            right = tiles[tile_idx+1]
        elif tile_idx == len(tiles)-1:
            right = False
            left = tiles[tile_idx-1]
        else:
            right = tiles[tile_idx+1]
            left = tiles[tile_idx-1]
        is_trap = False
        if left and center and not right:
            is_trap = True
        elif center and right and not left:
            is_trap = True
        elif left and not right and not center:
            is_trap = True
        elif right and not left and not center:
            is_trap = True
        result[tile_idx] = is_trap
    return result

def do_main(debug_mode=False):
    with open(Path('18/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('18/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    tiles = np.asanyarray([True if c == "^" else False for c in list(lines[0])], bool)

    count = 0
    for row in tqdm.tqdm(range(400000)):
        tiles = get_new_row(tuple(tiles))
        count += np.count_nonzero(tiles == False)
    print(count)

if __name__ == '__main__':
    do_main(False)