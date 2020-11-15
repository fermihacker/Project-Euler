from time import time

start = time()
sqSum = lambda n: sum([i**2 for i in range(n+1)])
sumSq = lambda n: sum(range(n+1))**2

ans = sumSq(100) - sqSum(100)

if __name__ == '__main__':
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")