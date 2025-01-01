


import functools
from hashlib import md5
import re


@functools.cache
def get_hash(salt, index):
    return md5((salt+str(index)).encode()).hexdigest()


def find_keys(salt, number_of_keys):
    keys = []
    index = 0
    while len(keys) != number_of_keys:
        hash = get_hash(salt, index)
        triplet = re.search(r"([a-z0-9])\1\1", hash)
        if triplet:
            is_key = False
            for i in range(1, 1001):
                hash2 = get_hash(salt, index+i)
                quint = re.search(rf"({triplet[1]})\1\1\1\1", hash2)
                if quint:
                    is_key = True
                    break
            if is_key:
                keys.append(index)
        index += 1
    return keys
            

def do_main(debug_mode=False):
    salt = "ngcjuoqr"    
    if debug_mode:
        salt = "abc"

    print(find_keys(salt, 64))
    

if __name__ == '__main__':
    do_main(True)