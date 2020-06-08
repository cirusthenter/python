def bin_search(x: list, key, first: int, last: int) -> int:
	if x[first] == key:
		return first
	if first == last:
		return -1
	mid = (first + last) // 2
	if key <= x[mid]:
		return bin_search(x, key, first, mid)	
	else:
		return bin_search(x, key, mid + 1, last)

if __name__ == "__main__":
	lst = [69, 145, 152, 176, 237, 242, 357, 490, 656, 706, 892, 1006, 1061, 1074, 1111, 1366, 1430, 1489, 1502, 1507, 1585, 1872, 1909, 1949, 2002, 2175, 2301, 2350, 2459, 2517, 2634, 2818, 2854, 2882, 3016, 3022, 3163, 3292, 3417, 3463, 3582, 3618, 3650, 3680, 3781, 3849, 4009, 4376, 4548, 4592, 4624, 4723, 4771, 4775, 4938, 5518, 5639, 5652, 5748, 5860, 5930, 5941, 5971, 5985, 6009, 6215, 6472, 6474, 6674, 6782, 6816, 6823, 6887, 7111, 7219, 7342, 7595, 7606, 7716, 7742, 7887, 7930, 7994, 8076, 8190, 8304, 8374, 8523, 8613, 8646, 9042, 9118, 9240, 9280, 9321, 9571, 9740, 9776, 9784, 9795]
	print(lst)
	while True:
		key = int(input("input the key: "))
		res = bin_search(lst, key, 0, 99)
		print("result:", res)
		if res != -1:
			print(f"lst[{res}] == {lst[res]}")
		else:
			print("Not Found")
