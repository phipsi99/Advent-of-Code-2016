from pathlib import Path
import re

def do_main(debug_mode=False):
    with open(Path('07/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('07/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    for line_index, line in enumerate(lines):
        abbas_inside = re.findall(r"\[[a-z]*([a-z])([a-z])\2\1[a-z]*]", line)
        abba_inside = False
        for abba in abbas_inside:
            if abba[0] != abba[1]:
                abba_inside = True
                break
        if abba_inside:
            continue
        abbas = re.findall(r"([a-z])([a-z])\2\1", line)
        abba_outside = False
        for abba in abbas:
            if abba[0] != abba[1]:
                point_sum += 1
                break


    point_sum = 0
    for line_index, line in enumerate(lines):
        abas = re.finditer(r"(?=([a-z])([a-z])\1)", line)
        brackets = re.finditer(r"(\[[a-z]*])", line)
        b_i = []
        for b in brackets:
            b_i.append(b.span(1))
        abas_outside = []
        abas_inside = []
        for aba in abas:
            was_inside = False
            for r in b_i:
                if aba.span(1)[0] in range(r[0], r[1]):
                    abas_inside.append(aba)
                    was_inside = True
                    break
            if not was_inside:
                abas_outside.append(aba)
                    
        ssl = False
        for aba in abas_outside:
            if aba[1] != aba[2]:
                for aba_i in abas_inside:
                    if aba[1] == aba_i[2] and aba[2] == aba_i[1]:
                        point_sum += 1
                        ssl = True
                        break
            if ssl:
                break

    print(point_sum)
        

if __name__ == '__main__':
    do_main(False)