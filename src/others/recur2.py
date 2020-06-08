from collections import deque
def recur2(n: int) -> None:
    stack = deque()
    while True:
        if n > 0:
            stack.append(n)
            n -= 1
            continue
        if stack:
            n = stack.pop()
            print(n, end='')
            n -= 2
            continue
        break
    print()


num = int(input("input an integer: "))
recur2(num)
