from functools import lru_cache
from time import time

@lru_cache
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

i, start = 0, time()
while len(str(fibonacci(i))) < 1000:
    i+=1

if __name__ == '__main__':
    print(f"\nAnswer: { i }")
    print(f"Time Taken: { time() - start }\n")