n = int(input())
times = []
for _ in range(n):
    time = list(map(int,input().split()))
    times.append(time)
times = sorted(times, key = lambda x: x[1])
ch = times[0]
k = 1
for i in range (1,n):
    if ch[0] > times[i][1] or ch[1] < times[i][0]:
        k +=1
        ch = times[i]
    else:
        continue
print(k)