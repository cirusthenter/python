from typing import List
import random
import time

def straight_insertionertion_sort(a: List[int]) -> List[int]:
	n = len(a)
	for i in range(1, n):
		val = a[i]
		for j in range(i, 0, -1):
			if a[j - 1] > val:
				a[j] = a[j - 1]
			else:
				a[j] = val
				break
		else:
			a[0] = val
	return a

if __name__ == "__main__":
	num = int(input("input an integer: "))
	l = [random.randint(0, num) for _ in range(num)]
	print(l)
	start = time.time()
	l = straight_insertionertion_sort(l)
	end = time.time()
	print(l)
	print(end - start)
