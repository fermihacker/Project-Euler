from time import time

start = time()
chamConst = ''.join(map(str, range(1000001)))
d = lambda n: int(chamConst[n])
ans = d(1)*d(10)*d(100)*d(1000)*d(10000)*d(100000)*d(1000000)

if __name__=="__main__":
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")