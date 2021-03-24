t = int(input())
while t > 0 :
    n = int(input())
    arr = list(map(int, input().rstrip().split(" ")))
    if n == 0:
        pass
    else:
        d = int(input())    
        arr1 = arr[::-1]
        arr2 = arr1[:n - d]
        arr3 = arr2[::-1]
        arr4 = arr1[n - d:]
        arr5 = arr4[::-1]
        arr = arr3 + arr5
        for i in range(n) : 
            print(arr[i], end = " ")
        print()
    
    t -= 1