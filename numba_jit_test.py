from numba import jit
from random import randint
import math
import time

NUMTIMES = 10000000

@jit (nopython=True)
def fast():
    x = []
    for i in range(NUMTIMES):
        r = randint(0,100)
        s = math.sqrt(r)
        x.append(s)
    return sum(x)/len(x)

def slow():
    x = []
    for i in range(NUMTIMES):
        r = randint(0,100)
        s = math.sqrt(r)
        x.append(s)
    return sum(x)/len(x)

def main():
    start = time.time()
    slow()
    end = time.time()
    print(f"SLOW Time elapsed:{end - start}")

    start = time.time()
    fast()
    end = time.time()
    print(f"FAST Time elapsed:{end - start}")

if __name__ == '__main__':
    main()
