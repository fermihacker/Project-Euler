from time import time

process = lambda n: n // 2 if n%2 == 0 else 3*n + 1

def collatz(n):
    s=[ n, ]
    while n > 1:
        n = process(n)
        s.append(n)
    s.append(1)
    return s

start = time()
res = [len(collatz(i)) for i in range(10**6)]
ans = res.index(max(res))       

if __name__ == '__main__':
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")


