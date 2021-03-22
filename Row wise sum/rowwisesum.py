p=int(input())
for i in range(p):
    str=input().split()
    n,m=int(str[0]),int(str[1])
    arr=[]
    for i in range(n):
        b=input().split()
        arrr=[int(x) for x in b]
        print(sum(arrr),end=" ")
    print()