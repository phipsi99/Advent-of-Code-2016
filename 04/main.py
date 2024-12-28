from pathlib import Path
from typing import Counter

def do_main(debug_mode=False):
    with open(Path('04/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('04/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        checksum = line[-6:-1]
        counts = Counter(line[:-11].replace('-', ''))
        l = list(counts.items())
        l.sort(key=lambda element: (-element[1], element[0]))
        counts = Counter(dict(l))
        top5 = counts.most_common(5)
        valid = True
        for index, (c, _) in enumerate(top5):
            if checksum[index] != c:
                valid = False 
        if valid:
            point_sum += int(line[-10:-7])

    print(point_sum)

    all_names = []

    for line_index, line in enumerate(lines):
        checksum = line[-6:-1]
        
        replacements = {}
        for char in range(ord("a"), ord("z") + 1):
            replacements[chr(char)] = chr((char - ord("a") + int(line[-10:-7])) % 26 + ord("a"))
        str_part = ""
        for c in line[:-11]:
            if c == "-":
                str_part += " "
            else:
                str_part += replacements[c]
        line = str_part + " " + line[-10:-7]
        all_names.append(line)

    for name in all_names:
        if "radioactive" in name:
            continue
        if "egg" in name:
            continue
        if "cookie" in name:
            continue
        if "marketing" in name:
            continue
        if "shipping" in name:
            continue
        if "testing" in name:
            continue
        print(name)

if __name__ == '__main__':
    do_main(False)