from time import time


def isLychrel(n):
	for i in range(50):
		n += int(str(n)[:: -1])
		if str(n) == str(n)[:: -1]:
			return False
	return True



start = time()
ans = sum(1 for i in range(10000) if isLychrel(i))

if __name__=="__main__":
   print(f"\nAnswer: { ans }")
   print(f"Time Taken: { time() - start }\n")
