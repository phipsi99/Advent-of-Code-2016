from pathlib import Path
import re

def recursive(line):
    pointer = 0
    total_len = 0
    while pointer < len(line):
        if line[pointer] == "(":
            marker = re.match(r"\((\d+)x(\d+)\)", line[pointer:])
            marker_end = marker.end() + pointer
            total_len += int(marker[2]) * recursive(line[marker_end:marker_end+int(marker[1])])
            pointer = marker_end + int(marker[1])
        else:
            pointer += 1
            total_len += 1
    return total_len
                

def do_main(debug_mode=False):
    with open(Path('09/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('09/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    line = lines[0]

    print(recursive(line))

if __name__ == '__main__':
    do_main(False)