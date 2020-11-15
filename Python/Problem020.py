from math import factorial
from time import time

digits = lambda n: map(int, list(str(n)))

start = time()
ans = sum(digits(factorial(100)))

if __name__ == '__main__':
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")
