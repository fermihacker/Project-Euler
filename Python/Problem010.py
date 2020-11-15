from math import sqrt; from itertools import count, islice
from time import time

def prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

start = time()
ans = sum(filter(lambda x: prime(x), range(2, 2*10**6)))

if __name__ == '__main__':
    start = time()
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")
