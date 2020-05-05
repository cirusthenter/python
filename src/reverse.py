import random
list = [random.randint(1, 9999) for _ in range(10)]
print("before sorted:", list)
list.sort()
print("after sorted:", list)
list.reverse()
print("after reversed:", list)
