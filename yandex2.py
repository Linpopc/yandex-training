import math
a,b,c,d = list(map(int, input().split()))
e = a * d + c * b
f = b * d
n = math.gcd(e,f)
print(e//n, f//n)
