from pathlib import Path

import numpy as np

def generate_data(initial_state, length):
    a = np.asanyarray([bool(int(i)) for i in  list(str(initial_state))], bool)
    while len(a) < length:
        b = a[::-1]
        b = ~b
        a = np.concatenate((np.append(a, False),b), axis=0)

    return a[:length]

def calc_checksum(data: np.ndarray):
    c = []
    while len(data) % 2 == 0:
        pairs = data.reshape(-1, 2)
        data = ~(pairs[:, 0] ^ pairs[:, 1])
    return data
    



def do_main(debug_mode=False):
    initial_state = 10010000000110000
    length = 272
    length2 = 35651584
    
    if debug_mode:
        initial_state = 10000
        length = 20

    point_sum = 0

    data = generate_data(initial_state, length)
    print("".join("1" if c else "0" for c in calc_checksum(data)))

    data = generate_data(initial_state, length2)
    print("".join("1" if c else "0" for c in calc_checksum(data)))



if __name__ == '__main__':
    do_main(False)