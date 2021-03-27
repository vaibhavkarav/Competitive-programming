f = 0
s = 1
t = 1

def checkMember(n):
    global f
    global s
    global t
    while t <= n:
      t = f + s
      f = s
      s = t
      if f == n:
        return 1
    pass

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")