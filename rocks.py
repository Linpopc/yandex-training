
def rocks (n,m):
    if n + m == 0:
        return 0
    R = []
    for _ in range (n+1):
        st = ['L'] * (m+1)
        R.append(st)
    for i in range (1,n+1):
        if R[i-1][0] == 'L' or R[i-2][0] == 'L' :
            R[i][0] = 'W'
        else:
            R[i][0] = 'L'
    for i in range (1,m+1):
        if R[0][i-1] == 'L' or R[0][i-2] == 'L':
            R[0][i] = 'W'
        else:
            R[0][i] = 'L'
    for i in range (1,n+1):
        for j in range (1,m+1):
            if R[i-1][j-1] == 'L' or R[i-1][j] == 'W' and R[i][j-1] == 'W':
                R[i][j] = 'L'
            else:
                R[i][j] = 'W'
    return R[n][m]
n,m = list(map(int,input().split()))
res = rocks(n,m)
if res == 'W':
    print('Win')
else:
    print('Loose')