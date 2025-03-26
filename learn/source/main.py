import time
import atexit


def clean_up():
    print('main clean up')


atexit.register(clean_up)

import tool

if __name__ == '__main__':
    st = time.time()
    while True:
        print('go')
        time.sleep(1)
        if time.time() - st > 10:
            c = 10 / 0
            break
