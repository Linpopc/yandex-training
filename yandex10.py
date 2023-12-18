def isGroup(k,a,b):
    groups = k//a
    if k % a <= groups * (b-a):
        return True
    return False
t = int(input())
for _ in range (t):
    n,a,b = list(map(int,input().split()))
    if isGroup(n,a,b):
        print('YES')
    else:
        print('NO')