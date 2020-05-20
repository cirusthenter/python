import random
import time
from typing import List

def shell_sort(a: List[int]) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            tmp = a[i]
            j = i - h
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

def shell_sort2(a: List[int]) -> None:
    n = len(a)
    h = 1
    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //=  3

if __name__ == "__main__":
    num = int(input("number of elements: "))
    x1 = [random.randint(0, num) for _ in range(num)]
    x2 = x1.copy()    
    x3 = x1.copy()

    start1 = time.time()
    shell_sort(x1)
    end1 = time.time()

    start2 = time.time()
    shell_sort2(x2)
    end2 = time.time()

    start3 = time.time()
    x3.sort()
    end3 = time.time()

    print("result:", "success" if x1 == x2 == x3 else "failed")
    print("naive:", end1 - start1)
    print("better shell:", end2 - start2)
    print("library:", end3 - start3)
