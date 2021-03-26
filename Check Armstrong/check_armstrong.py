def armstrong(n):
    d = 0
    temp = n
    while temp > 0:
        temp = temp // 10
        d = d + 1
    arm = 0
    while n > 0:
        rem = n % 10
        arm = arm + rem ** d 
        n = n // 10
    return arm

n = int(input())
temp = n
x = armstrong(n)
if temp == x:
    print("true")
else:
    print("false")