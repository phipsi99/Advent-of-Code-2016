from pathlib import Path

from tqdm import tqdm

def process(code, reg_a = 0):
    registers = {"a": reg_a, "b": 0, "c": 0, "d": 0}
    func_pointer = 0
    out = []
    c = 0
    while func_pointer < len(code) and c < 50000:
        c += 1
        instruction = code[func_pointer]
        if "cpy" in instruction:
            val = instruction.split(" ")[1]
            reg = instruction.split(" ")[2]
            try:
                val = int(val)
            except ValueError:
                val = registers[val]
            registers[reg] = val
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
            if cond == "0":
                func_pointer += 1
                continue
            if cond == "1" or registers[cond] != 0:
                try:
                    val = int(val)
                except ValueError:
                    val = registers[val]
                func_pointer += val
            else:
                func_pointer += 1
        elif "tgl" in instruction:
            val = registers[instruction.split(" ")[1]]
            if 0 > (func_pointer + val) or len(code) <= (func_pointer + val):
                func_pointer += 1
                continue
            instruction_to_be_toggled = code[func_pointer + val]
            if "inc" in instruction_to_be_toggled:
                code[func_pointer + val] = instruction_to_be_toggled.replace("inc", "dec")
            elif "dec" in instruction_to_be_toggled:
                code[func_pointer + val] = instruction_to_be_toggled.replace("dec", "inc")
            elif "jnz" in instruction_to_be_toggled:
                code[func_pointer + val] = instruction_to_be_toggled.replace("jnz", "cpy")
            elif "cpy" in instruction_to_be_toggled:
                code[func_pointer + val] = instruction_to_be_toggled.replace("cpy", "jnz")
            elif "tgl" in instruction_to_be_toggled:
                code[func_pointer + val] = instruction_to_be_toggled.replace("tgl", "inc")
            func_pointer += 1
        elif "out" in instruction:
            val = instruction.split(" ")[1]
            try:
                val = int(val)
            except ValueError:
                val = registers[val]
            out.append(val)
            func_pointer += 1
    return out

def alternating(l):
  for i in range(1, len(l) - 1):
    if not (l[i - 1] < l[i] > l[i + 1] or
            l[i - 1] > l[i] < l[i + 1]):
      return False
  return True

def do_main(debug_mode=False):
    with open(Path('25/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('25/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for i in tqdm(range(0, 250)):
        out = process(lines, i)
        if out:
            if set(out) == {0, 1} and alternating(out):
                print()
                print(i)
                print(out)


if __name__ == '__main__':
    do_main(False)