from time import time

isPall = lambda s : str(s)==str(s)[::-1]

start = time()
ans = max([i*j for (i,j) in enumerate(list(range(100,1001)),100) if isPall(i*j)])

if __name__ == "__main__":
    print(f"\nAnswer: { ans }")
    print(f"Time taken: { time() - start }\n")
