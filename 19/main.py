
def do_main(debug_mode=False):
    no_elfs = 3018458
    
    if debug_mode:
        no_elfs = 5

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
        
    

if __name__ == '__main__':
    do_main(False)