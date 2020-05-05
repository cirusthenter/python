import random
from max import max_of

print("max limit")
num = int(input("number of random int: "))
lo = int(input("min: "))
hi = int(input("max: "))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(f'{(x)}')
print(f'max value: {max_of(x)}')
