from time import time

counter = 0

for i in range(100):
    for j in range(100):
        if len(str(i**j)) == j:
            counter += 1

if __name__=="__main__":
    start = time()
    print(f"\nAnswer: { counter - 1 }") # the -1 is for "1" 
    print(f"Time Taken: { time() - start }\n")