from sys import stdin 
MIN_VALUE = -2147483648 
def secondLargestElement(arr, n):
    if n == 0 : 
        return MIN_VALUE
    p = max(arr)
	arr.remove(p)
	n = max(arr)
    return n 
def takeInput() :
    n = int(input()) 
    if n != 0: 
        arr = list(map(int, input().rstrip().split(" "))) 
        return arr, n
    return list(), 0
t = int(input().rstrip()) 
while t > 0 :
    arr, n = takeInput()
    print(secondLargestElement(arr, n)) 
    
    t -= 1