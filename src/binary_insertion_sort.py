from typing import List
import time
import random
import bisect


def binary_insertion_sort(a: List[int]) -> None:
    n = len(a)
    for i in range(1, n):
        val = a[i]
        left, right = 0, i - 1
        while True:
            if left == right:
                if a[left] <= val:
                    p = left + 1
                else:
                    p = left
                break
            if left + 1 == right:
                if val < a[left]:
                    p = left
                elif val < a[right]:
                    p = right
                else:
                    p = right + 1
                break
            mid = (left + right) // 2
            if val <= a[mid]:
                right = mid
                continue
            else:
                left = mid + 1
                continue
        for j in range(i, p, -1):
            a[j] = a[j - 1]
        a[p] = val


def binary_insertion_sort2(a: List[int]) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)


def binary_insertion_sort3(a: List[int]) -> None:
    """２分挿入ソート"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # 探索範囲の先頭要素の添字
        pr = i - 1  # 探索範囲の末尾要素の添字

        while True:
            pc = (pl + pr) // 2     # 探索範囲の中央要素の添字
            if a[pc] == key:        # 探索成功
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        # 挿入すべき位置の添字
        pd = pc + 1 if pl <= pr else pr + 1

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key
    return a


if __name__ == "__main__":
    import copy
    num = int(input("input an integer: "))
    l = [random.randint(0, num) for _ in range(num)]
    start = time.time()
    b = copy.copy(l)
    binary_insertion_sort3(b)
    end = time.time()
    print(l)
    print(b)
    print(end - start)
