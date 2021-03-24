from sys import stdin
def sort012(arr, n) :
    nextZero = 0
    nextTwo = (n - 1) 
    i = 0 
    while i <= nextTwo :
        if arr[i] == 0 :
            arr[i], arr[nextZero] = arr[nextZero], arr[i]
            i += 1
            nextZero += 1
        elif arr[i] == 2 :
            arr[i], arr[nextTwo] = arr[nextTwo], arr[i]
            nextTwo -= 1
        else : 
            i += 1 
def takeInput() : 
    n = int(input().rstrip())
    if n == 0 :
        return list(), 0 
    arr = list(map(int, input().rstrip().split(" ")))
    return arr, n
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print() 
t = int(input())
while t > 0 :
    arr, n = takeInput() 
    sort012(arr, n)
    printList(arr, n) 
    t -= 1