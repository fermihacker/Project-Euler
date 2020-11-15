from time import time

pall = lambda n : str(n) == str(n)[::-1]
check = lambda n : pall(n) and pall(bin(n).replace('0b', ''))
start = time()
ans = sum([i for i in range(1,10**6) if check(i)])

if __name__=="__main__":
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")

