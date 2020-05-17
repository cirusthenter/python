from typing import List
import random
import time


def selection_sort(a: List[int]) -> List[int]:
    n = len(a) - 1
    for i in range(n):
        min = a[i]
        min_index = i
        for j in range(i + 1, n + 1):
            if min > a[j]:
                min = a[j]
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


if __name__ == "__main__":
    num_cnt = int(input("Input an intenger: "))
    l = [random.randint(0, num_cnt) for _ in range(num_cnt)]
    print(l)
    start = time.time()
    l = selection_sort(l)
    end = time.time()
    print(l)
    print(end - start)
