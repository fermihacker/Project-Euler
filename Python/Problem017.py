import num2words
from time import time

start = time.time()
word = lambda k : num2words.num2words(k).replace(' ', '').replace('-', '')
p = ''

for i in range(1, 1001):
    p += word(i)
    
ans = len(p)

if __name__ == '__main__':
    print(f"\nAnswer: { ans }")
    print(f"Time Taken: { time() - start }\n")
