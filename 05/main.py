import hashlib

def do_main(debug_mode=False):
    #door_id = "abc"
    door_id = "wtnhxymk"

    found_keys = []
    idx = 0
    while len(found_keys) < 8:
        key = hashlib.md5((door_id+str(idx)).encode()).hexdigest()
        if key.startswith("00000"):
            found_keys.append(key[5])
        idx += 1

        
    print("".join(found_keys))


if __name__ == '__main__':
    do_main(False)