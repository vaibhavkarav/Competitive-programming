N = int(input())
a = N
b = N - 1
for i in range(1, a + 1, 1):
    for j in range(1, i):
        print(' ', end = '')
    for j in range(i, a + 1):
        print(j, end = '')
    print()
for i in range(b, 0, -1):
    for j in range(1, i):
        print(' ', end = '')
    for j in range(i, a + 1):
        print(j, end = '')
    print()