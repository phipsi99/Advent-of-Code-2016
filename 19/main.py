
import math

import pandas as pd



def print_circle2(no_elfs):
    elfs = pd.Series(range(1, no_elfs+1))
    index = 0
    while len(elfs) != 1:        
        next_elf = (index + len(elfs) //2) % len(elfs)
        elfs.pop(next_elf)
        if next_elf > index:
            index = (index + 1) % len(elfs)
        else:
            index %= len(elfs)
        elfs.reset_index(inplace=True, drop=True)
    print(f"{no_elfs}: {elfs[0]}")


def print_circle(no_elfs):
    elfs = [1] * no_elfs
    index = 0
    while elfs.count(no_elfs) != 1:
        if elfs[index] == 0:
            index = (index +1) %no_elfs
            continue
        
        next_elf = (index + 1) % no_elfs
        while elfs[next_elf] == 0:
            next_elf = (next_elf + 1) % no_elfs
        elfs[index] += elfs[next_elf]
        elfs[next_elf] = 0
        index = (index +1) %no_elfs

    print(elfs)

def do_main(debug_mode=False):
    no_elfs = 3018458
    
    if debug_mode:
        no_elfs = 97

    k = math.floor(math.log2(no_elfs))
    p = 2 ** k
    r = no_elfs - p
    index = 2 * r
    print(index+1)

    starts = [1, 2, 4]
    while starts[-1] < no_elfs:
        diff = starts[-1] - starts[-2]
        diff *= 3
        starts.append(starts[-1] + diff)

    if no_elfs < (starts[-1] - starts[-2]):
        print(no_elfs - starts[-2] +1)
    

    
    

if __name__ == '__main__':
    do_main(False)