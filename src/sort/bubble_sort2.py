from typing import List
import random
import time

def bubble_sort2(a: List[int]) -> List:
	n = len(a)
	for i in range(n - 1):
		exchange = False
		for j in range(n - 1, i, -1):
			if a[j - 1] > a[j]:
				a[j - 1], a[j] = a[j], a[j - 1]
				exchange = True
		if not exchange:
			break
	return a

if __name__ == "__main__":
	num_cnt = int(input("Input an intenger: "))
	l = [random.randint(0, num_cnt) for _ in range(num_cnt)]
	l.sort()
	start = time.time()
	l = bubble_sort2(l)
	end = time.time()
	print(end - start)
