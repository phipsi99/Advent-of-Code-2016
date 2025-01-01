from pathlib import Path
import re

def process(code):
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    func_pointer = 0
    while func_pointer < len(code):
        instruction = code[func_pointer]
        if "cpy" in instruction:
            val = instruction.split(" ")[1]
            reg = instruction.split(" ")[2]
            if val.isnumeric():
                registers[reg] = int(val)
            else:
                registers[reg] = registers[val]
            func_pointer += 1
        elif "inc" in instruction:
            reg = instruction.split(" ")[1]
            registers[reg] +=1
            func_pointer += 1
        elif "dec" in instruction:
            reg = instruction.split(" ")[1]
            registers[reg] -=1
            func_pointer += 1
        elif "jnz" in instruction:
            cond = instruction.split(" ")[1]
            val = instruction.split(" ")[2]
            if cond == "1" or registers[cond] != 0:
                func_pointer += int(val)
            else:
                func_pointer += 1
    return registers



def do_main(debug_mode=False):
    with open(Path('12/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('12/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    print(process(lines))

if __name__ == '__main__':
    do_main(False)