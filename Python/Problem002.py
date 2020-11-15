from functools import lru_cache
from time import time

@lru_cache
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
start = time()
i, ans = 0, 0
while (k := fibonacci(i)) < 4*10**6:
    if k%2==0:
        ans += k
    i += 1

if __name__ == '__main__':
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")
