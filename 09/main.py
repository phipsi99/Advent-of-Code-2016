from pathlib import Path
import re

def do_main(debug_mode=False):
    with open(Path('09/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('09/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    line = lines[0]

    markers_matches= re.finditer(r"\((\d+)x(\d+)\)", line)
    decompressed = ""
    raw_markers = []
    for marker in markers_matches:
        raw_markers.append(marker)

    markers = []
    for i, marker in enumerate(raw_markers):
        in_other = False
        # for m in markers [:i]:
        #     end = m.end()+ int(m[1])
        #     if marker.start() < end:
        #         in_other = True
        #         break
        if not in_other:
            markers.append(marker)

    for marker_index in range(len(markers)):
        if marker_index == 0:
            string_up_to_marker = line[:markers[marker_index].start()]
        else:
            string_up_to_marker = line[markers[marker_index-1].end() + int(markers[marker_index-1][1]): markers[marker_index].start()]
        decompressed += string_up_to_marker
        string_to_repeat = line[markers[marker_index].end():markers[marker_index].end()+int(markers[marker_index][1])]
        decompressed += string_to_repeat * int(markers[marker_index][2])
    decompressed +=  line[markers[-1].end()+ int(markers[-1][1]):]

    print(decompressed)
    print(len(decompressed))

if __name__ == '__main__':
    do_main(True)