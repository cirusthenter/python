from typing import List
import time
import random

def quick_sort(left: int, right: int, a: List[int]) -> None:
    pivot = a[(left + right) // 2]
    pl = left
    pr = right
    print(f'a[{left}] - a[{right}]:', *a[left:right + 1])
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
        quick_sort(left, pr, a)
    if pl < right:
        quick_sort(pl, right, a) 

if __name__ == "__main__":
    num = int(input("number of elements: "))
    x1 = [random.randint(0, num) for _ in range(num)]
    x3 = x1.copy()

    start1 = time.time()
    quick_sort(0, len(x1) - 1, x1)
    end1 = time.time()

    start3 = time.time()
    x3.sort()
    end3 = time.time()

    print("result:", "success" if x1 == x3 else "failed")
    print("my qucik sort:", end1 - start1)
    print("library:", end3 - start3)
