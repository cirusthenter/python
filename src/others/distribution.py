ans = [0] * 36
for i in range(1, 7):
    for j in range(1, 7):
        ans[i*j - 1] += 1

for i in range(36):
    print(i+1, '|', end='')
    for j in range(ans[i]):
        print("*************************", end='')
    print()
