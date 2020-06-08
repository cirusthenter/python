def euclids_algo(m: int, n: int) -> int:
    large = max(m, n)
    small = min(m, n)
    if large % small == 0:
        return small
    return euclids_algo(small, large % small)

if __name__ == "__main__":
    left = int(input("m: "))
    right = int(input("n: "))
    print(f'gcd({left}, {right}) = {euclids_algo(left, right)}')
