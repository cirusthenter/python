from typing import List
import random
import time


def shaker_sort(a: List[int]) -> List[int]:
    left = 0
    right = len(a) - 1
    while left < right:
        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        right -= 1
        for i in range(right, left, -1):
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
        left += 1
    return a


if __name__ == "__main__":
    num_cnt = int(input("Input an intenger: "))
    l = [random.randint(0, num_cnt) for _ in range(num_cnt)]
    print(l)
    start = time.time()
    l = shaker_sort(l)
    end = time.time()
    print(l)
    print(end - start)
