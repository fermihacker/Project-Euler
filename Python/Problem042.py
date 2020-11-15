from time import time

T = lambda n : n * (n + 1) // 2
tNums = [T(i) for i in range(1000)]
nameNum = lambda s : sum([ord(i) - 64 for i in s])
check = lambda s : nameNum(s) in tNums

def getWords():
    tempStr = ''    
    with open('p042_words.txt', 'r') as f:
        tempStr = ''.join(f.readlines())
    out = tempStr.split(',')
    return sorted([i[1:len(i)-1] for i in out])

start = time() 
ans = sum([1 for i in getWords() if check(i)])

if __name__=="__main__":    
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")


