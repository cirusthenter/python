import time
from typing import List
import random
from collections import deque

def quick_sort(a: List[int]) -> None:
    left = 0
    right = len(a) - 1
    stk = deque()
    stk.append((left, right))
    while stk:
        popped = stk.pop()
        left = popped[0]
        right = popped[1]
        pl = left
        pr = right
        pivot = a[(left + right) // 2]
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
            stk.append((left, pr))
        if pl < right:
            stk.append((pl, right))

num = int(input("input an integer: "))
x = [random.randint(0, num) for _ in range(num)]
x2 = x.copy()

start1 = time.time()
quick_sort(x)
end1 = time.time()

start2 = time.time()
x2.sort()
end2 = time.time()

print("result:", "success" if x == x2 else "failed")
print("mine:", end1 - start1)
print("STL:", end2 - start2)
