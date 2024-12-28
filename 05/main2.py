import hashlib
from concurrent.futures import ThreadPoolExecutor

def find_valid_key(door_id, start_idx, end_idx):
    results = []
    for idx in range(start_idx, end_idx):
        key = hashlib.md5((door_id + str(idx)).encode()).hexdigest()
        if key.startswith("00000"):
            position = key[5]
            if position.isnumeric() and 0 <= int(position) < 8:
                results.append((int(position), key[6]))
    return results

def do_main(debug_mode=False):
    door_id = "wtnhxymk"
    found_keys = [None] * 8
    idx = 0
    step = 100000  
    
    while None in found_keys:
        with ThreadPoolExecutor(max_workers=4) as executor:
            ranges = [(i, i + step) for i in range(idx, idx + step * 4, step)]
            results = executor.map(lambda r: find_valid_key(door_id, *r), ranges)
            for result in results:
                for position, char in result:
                    if found_keys[position] is None:
                        found_keys[position] = char
                        print(found_keys)
        idx += step * 4 

    print("".join(found_keys))

if __name__ == '__main__':
    do_main(False)
