N = int(input())
ar = list(map(int,input().split()))
def merge(a,b):
    i = 0
    j = 0
    n = 0
    n1 = len(a)
    n2 = len(b)
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

def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    a = array[0:n//2]
    b = array[n//2:n]
    a = merge_sort(a)
    b = merge_sort(b)
    return merge(a,b)

res = merge_sort(ar)
for i in res:
    print(i, end = " ")

