from collections import defaultdict
from pathlib import Path
import re

def do_main(debug_mode=False):
    with open(Path('10/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('10/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    bots = defaultdict(list)
    outputs = [0]*1000

    raw_instructions = lines[:]
    instructions = []
    for instruction in raw_instructions:
        if "goes" in instruction:
            value, bot = re.findall(r"\d+", instruction)
            bots[bot].append(int(value))
        else:
            instructions.append(instruction)


    while len(instructions) > 0:
        current_instruction = instructions.pop(0)
        bot, low, high = re.findall(r"\d+", current_instruction)
        if len(bots[bot]) == 2:
            low_val, high_val = sorted(int(i) for i in bots[bot])
            if low_val == 17 and high_val == 61:
                print(bot)
            if "low to output" in current_instruction:
                outputs[int(low)] = low_val
            else:
                bots[low].append(low_val)
            if "high to output" in current_instruction:
                outputs[int(high)] = high_val
            else:
                bots[high].append(high_val)
            bots[bot] = []
        else:
            instructions.append(current_instruction)
    print(outputs[0] * outputs[1] * outputs[2])
            



        

if __name__ == '__main__':
    do_main(False)