import time
from typing import List
import random

def quick_sort(a: List[int], left: int, right: int) -> None:
    pivot = a[(left + right) // 2]
    pl = left
    pr = right
    while pl <= pr:
        while a[pl] < pivot:
            pl += 1
        while pivot < a[pr]:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    if left < pr:
        quick_sort(a, left, pr)
    if pl < right:
        quick_sort(a, pl, right)

num = int(input("input an integer: "))
x = [random.randint(0, num) for _ in range(num)]
x2 = x.copy()

start1 = time.time()
quick_sort(x, 0, num - 1)
end1 = time.time()

start2 = time.time()
x2.sort()
end2 = time.time()

print("result:", "success" if x == x2 else "failed")
print("mine:", end1 - start1)
print("STL:", end2 - start2)
