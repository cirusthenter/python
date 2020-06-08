import time
from typing import List, MutableSequence
import random
import heapq

def heap_sort(a: List[int]) -> None:
    # make it to heap
    for i, elem in enumerate(a):
        j = i
        parent = (j - 1) // 2
        while parent >= 0:
            if a[parent] < elem:
                a[j] = a[parent]
            else:
                a[j] = elem
                break
            j = parent
            parent = (j - 1) // 2
        else:
            a[0] = elem

    # sort it
    for i in range(len(a) - 1, -1, -1):
        elem = a[i]
        a[i] = a[0]
        j = 0
        cl = 1
        cr = 2
        while cl < i:
            if cr >= i:
                child = cl
            elif a[cl] < a[cr]:
                child = cr
            else:
                child = cl
            if elem < a[child]:
                a[j] = a[child]
                j = child
                cl = 2 * j + 1
                cr = 2 * j + 2
            else:
                a[j] = elem
                break
        else:
            a[j] = elem


def heap_sort_text(a: MutableSequence) -> None:
    """ヒープソート"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left]～a[right]をヒープ化"""
        temp = a[left]      # 根

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 左の子
            cr = cl + 1             # 右の子
            child = cr if cr <= right and a[cr] > a[cl] else cl  # 大きいほう
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # a[i]～a[n-1]をヒープ化
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # 最大要素と未ソート部末尾要素を交換
        down_heap(a, 0, i - 1)      # a[0]～a[i-1]をヒープ化

def heapq_sort(a: List[int]) -> None:
    heap = []
    for i in a:
        heapq.heappush(heap, i)
    for i in range(len(a)):
        a[i] = heapq.heappop(heap)


num = int(input("input an integer: "))
x = [random.randint(0, num) for _ in range(num)]
x2 = x.copy()
x3 = x2.copy()
x4 = x3.copy()

start1 = time.time()
heap_sort(x)
end1 = time.time()

start2 = time.time()
heap_sort_text(x2)
end2 = time.time()

start3 = time.time()
heapq_sort(x3)
end3 = time.time()

start4 = time.time()
x4.sort()
end4 = time.time()

print("result:", "success" if x == x2 == x3 else "failed")
print("mine:", end1 - start1)
print("text:", end2 - start2)
print("heapq:", end3 - start3)
print("STL:", end4 - start4)

