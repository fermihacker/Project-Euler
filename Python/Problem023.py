from math import sqrt
from time import time
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

start = time()
temp_list = list(i for i in range(1, 28123) if sum(factors(i)) > i)
notAbundant = list(i for i in range(1, 28123))

for i in range(len(temp_list)):
	for j in range(i, 28123):
		if temp_list[i] + temp_list[j] < 28123:
			notAbundant[temp_list[i] + temp_list[j]] = 0
		else:
			break

ans = sum(notAbundant)

if __name__ == "__main__":
    start = time()
    print(f"\nAnswer: { ans }")
    print(f"Time taken:{ time() - start }\n")
