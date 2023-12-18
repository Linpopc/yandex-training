import math
x1, y1, x2, y2 = list(map(float,input().split()))

def S1(x1, y1, x2, y2):
    R = math.sqrt(x2**2 + y2**2)
    r = math.sqrt(x1**2 + y1**2)
    l = abs(R-r)
    deg = math.atan2(y1,x1) - math.atan2(y2,x2)
    S = l + abs((2*math.pi*r)/math.radians(360) * deg)
    S2 = l + abs((2*math.pi*R)/math.radians(360) * deg)
    return abs(min(round(S, 12),round(S2, 12)))

def S2 (x1, y1, x2, y2):
    R = math.sqrt(x1**2 + y1**2)
    r = math.sqrt(x2**2 + y2**2)
    S = R + r
    return S

degr1 = math.atan2(y1,x1)
degr2 = math.atan2(y2,x2)
res = 0
if degr1 == degr2 or x1==0 and y1 == 0:
    res = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
else:
    res = min(S2(x1, y1, x2, y2 ), S1(x1, y1, x2, y2 ))
print(abs(res))