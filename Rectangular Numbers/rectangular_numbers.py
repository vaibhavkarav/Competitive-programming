n = int(input())
temp = n

for i in range(1,n+1):
    for j in range(1, i, 1):
        for x in range(1, i, 2*i):
            print(n-j+1, end = '')
    for k in range(2*n - 2*i + 2, 1, -1):
        print(temp, end = '') 
    temp = temp - 1
    for j in range(i, 1, -1):
        for x in range(1, i, 2*i):
            print(n-j+2, end = '') 
    print()
    
temp = 2
for i in range(n, 1, -1):
    for j in range(2, i, 1):
        print(n - j + 2, end = '')
    for k in range(2*n - i , i-3, -1):
        print(temp, end = '')
    for x in range(i-1, 1, -1):
        print(n - x + 2, end = '')
    temp = temp + 1
    print()