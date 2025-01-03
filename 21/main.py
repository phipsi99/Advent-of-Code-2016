from itertools import combinations
from pathlib import Path
from random import shuffle
import re

def unscramble(lines, password):
    for line_index, line in enumerate(lines):
        if "swap position" in line:
            i1, i2 = [int(i) for i in re.findall(r"\d", line)]
            temp = password[i1]
            password[i1] = password[i2]
            password[i2] = temp
        elif "swap letter" in line:
            i1, i2 = [password.index(i) for i in re.findall(r"\b[a-z]\b", line)]
            temp = password[i1]
            password[i1] = password[i2]
            password[i2] = temp
        elif "rotate based" in line:
            steps = password.index(re.findall(r"\b[a-z]\b", line)[0])
            if steps >= 4:
                steps += 1
            steps += 1
            for i in range(steps):
                p = password.pop()
                password.insert(0, p)
        elif "rotate" in line:
            steps = int(re.findall(r"\d", line)[0])
            if "left" in line:
                for i in range(steps):
                    p = password.pop(0)
                    password.append(p)
            else:
                for i in range(steps):
                    p = password.pop()
                    password.insert(0, p)
        elif "reverse" in line:
            x,y = [int(i) for i in re.findall(r"\d", line)]
            before = password[:x]
            middle = password[x:y+1]
            after = password[y+1:]
            middle.reverse()
            password = before + middle + after
        elif "move" in line:
            x,y = [int(i) for i in re.findall(r"\d", line)]
            temp = password.pop(x)
            password.insert(y, temp)
    return password

def do_main(debug_mode=False):
    with open(Path('21/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    password = list("abcdefgh")
    
    if debug_mode:
        with open(Path('21/test.txt')) as file:
            lines = [line.rstrip() for line in file]
        password = list("abcde")

    point_sum = 0

    print("".join(unscramble(lines, password)))

    found_pw = ""
    orig = list("abcdefgh")
    while found_pw != "fbgdceah":
        shuffle(orig)
        found_pw = unscramble(lines, orig)
    print(orig)

                

if __name__ == '__main__':
    do_main(False)