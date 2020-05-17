def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return factorial(n - 1) * n

if __name__ == "__main__":
    num = int(input())
    print(f'{num}! = {factorial(num)}')
