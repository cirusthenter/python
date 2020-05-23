from typing import List, MutableSequence
import time
import random

def counting_sort(a: List[int]) -> None:
    counts = [0] * (max(a) + 1)
    for i in a:
        counts[i] += 1
    i = 0
    for elem, count in enumerate(counts):
        for _ in range(count):
            a[i] = elem
            i += 1

def fsort(a: MutableSequence, max: int) -> None:
    """度数ソート（配列要素の値は0以上max以下）"""
    n = len(a)
    f = [0] * (max + 1)     # 累積度数
    b = [0] * n             # 作業用目的配列

    for i in range(n):             f[a[i]] += 1                     # [Step 1]
    for i in range(1, max + 1):    f[i] += f[i - 1]                 # [Step 2]
    for i in range(n - 1, -1, -1): f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [Step 3]
    for i in range(n):             a[i] = b[i]                      # [Step 4]

def counting_sort_text(a: MutableSequence) -> None:
    """度数ソート"""
    fsort(a, max(a))

num = int(input("input an integer: "))
x1 = [random.randint(0, num) for _ in range(num)]
x2 = x1.copy()
x3 = x2.copy()

start1 = time.time()
counting_sort(x1)
end1 = time.time()

start2 = time.time()
counting_sort_text(x2)
end2 = time.time()

start3 = time.time()
x3.sort()
end3 = time.time()

print("result:", "success" if x1 == x2 == x3 else "failed")
print("my counting_sort:", end1 - start1)
print("text:", end2 - start2) 
print("STL:", end3 - start3)
