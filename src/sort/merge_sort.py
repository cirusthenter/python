from typing import List
import random
import time

def merge_sort(a: List[int]) -> None:
    def _merge_sort(a: List[int], left: int, right: int) -> None:
        if left >= right:
            return
        center = (left + right) // 2
        _merge_sort(a, left, center)
        _merge_sort(a, center + 1, right)
        buff = a[left: center + 1].copy()
        left_offset = right_offset = 0
        left_index = left
        right_index = center + 1
        while left_index <= center and right_index <= right:
            if buff[left_offset] < a[right_index]:
                a[left + left_offset + right_offset] = buff[left_offset]
                left_offset += 1
                left_index += 1
            else:
                a[left + left_offset + right_offset] = a[right_index]
                right_offset += 1
                right_index += 1
        while left_index <= center:
            a[left + left_offset + right_offset] = buff[left_offset]
            left_offset += 1
            left_index += 1
    _merge_sort(a, 0, len(a) - 1)

if __name__ == "__main__":
    num = int(input("number of elements: "))
    x1 = [random.randint(0, num) for _ in range(num)]
    x3 = x1.copy()

    start1 = time.time()
    merge_sort(x1)
    end1 = time.time()

    start3 = time.time()
    x3.sort()
    end3 = time.time()

    print("result:", "success" if x1 == x3 else "failed")
    print("my qucik sort:", end1 - start1)
    print("library:", end3 - start3)
