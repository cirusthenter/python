from typing import Any, Sequence


def max_of(a: Sequence) -> Any:
    # """ Return the max of sequence a """
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == "__main__":
    print('max value of an array')
    num = int(input('number of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    print(f"max value is {max_of(x)}")
