from time import time

start = time()
ans = sum(map(int, [i for i in str(2**1000)]))

if __name__ == '__main__':
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")