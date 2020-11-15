from time import time

start = time()
ans = sum([i**i for i in range(1, 1000)])%(10**10)

if __name__=="__main__":    
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")
