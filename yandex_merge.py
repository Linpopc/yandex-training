n1 = int(input())
a = list(map(int,input().split())) if n1>0 else input()
n2 = int(input())
b = list(map(int,input().split())) if n2>0 else input()

def merge(a,b):
    i = 0
    j = 0
    n = 0
    res = [0] * (n1+n2)
    while (i < n1 or j < n2):
        if j>=n2 or i < n1 and a[i] < b[j]:
            res[n]=a[i]
            i+=1
        else:
            res[n]=b[j]
            j+=1
        n+=1
    return res
res = merge(a,b)
for i in res:
    print(i, end = ' ')

