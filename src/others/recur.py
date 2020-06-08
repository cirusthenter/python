def recur(n: int) -> int:
    if n > 0:
        recur(n - 1)
        print(n, end='')
        recur(n - 2)
    
x = int(input("input an integer: "))
recur(x)
print()
