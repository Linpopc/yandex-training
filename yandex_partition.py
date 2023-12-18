import random as rnd
n = int(input())
array = list(map(int,input().split())) if n>0 else input()

def partition(x,l,r):
    m = l
    for i in range (l, r):
        if array[i] <= x:
            array[i], array[m] = array[m], array[i]
            m+=1
    return m

def sort(l,r):
    if r - l<= 1:
        return
    x = array[rnd.randint(l,r-1)]
    m = partition(x,l,r)
    sort(l,m)
    sort(m,r)

sort(0,n)

print(array)

