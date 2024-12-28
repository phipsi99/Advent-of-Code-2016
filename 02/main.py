# 13:26 min
from pathlib import Path

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

keypad2 = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0]
]

def do_main(debug_mode=False):
    with open(Path('02/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('02/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    dirs = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    pw = ""
    pw2 = ""
    
    cursor = (1, 1)
    for line_index, line in enumerate(lines):
        for c in line:
            cursor = (cursor[0] + dirs[c][0], cursor[1] + dirs[c][1])
            cursor = (max(0, min(cursor[0], 2)), max(0, min(cursor[1], 2)))
        key = keypad[cursor[1]][cursor[0]]
        pw += str(key)
        
    cursor = (0, 2)
    for line_index, line in enumerate(lines):
        for c in line:
            new_cursor = (cursor[0] + dirs[c][0], cursor[1] + dirs[c][1])
            if 0 <= new_cursor[0] < len(keypad2[0]) and 0 <= new_cursor[1] < len(keypad2) and keypad2[new_cursor[1]][new_cursor[0]] != 0:
                cursor = new_cursor
        key = keypad2[cursor[1]][cursor[0]]
        pw2 += str(key)
    print(pw)
    print(pw2)
        



if __name__ == '__main__':
    do_main(False)