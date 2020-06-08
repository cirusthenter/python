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
if __name__ == "__main__":
    print("shell sort")
    num = int(input("number of elements: "))
    x = [random.randint(0, num) for _ in range(num)]
    print(x)
    
    start = time.time()
    shell_sort(x)
    end = time.time()

    print("sorted!")
    print(x)
    print(end - start)
