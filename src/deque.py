from collections import deque

d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
K = int(input())
for _ in range(K):
    val = d.popleft()
    first = val % 10
    ten_times = val * 10
    if first != 0:
        d.append(ten_times + first - 1)
    d.append(ten_times + first)
    if first != 9:
        d.append(ten_times + first + 1)
print(val)