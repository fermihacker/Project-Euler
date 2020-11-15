from math import factorial 
from time import time


digit_fact_sum = lambda n : sum( factorial( int( i ) ) for i in str(n) )


def check_chain(n):
    refLis, i = [n], n
    counter = 0
    if n == digit_fact_sum(n):
        return 1
    while True:
        i = digit_fact_sum(i)
        refLis.append(i)
        counter += 1
        if list(dict.fromkeys(refLis)) != refLis:
            return counter 


def main():
    counter = 0
    for i in range(1, 10**6 + 1):
        if check_chain(i) == 60:
            counter += 1
    return counter


if __name__=="__main__":
    start = time()
    print(f"\nAnswer: { main() }")
    print(f"Time Taken: { time() - start }\n")

