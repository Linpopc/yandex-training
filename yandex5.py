n = int(input())
ratings = list(map(int, input().split()))

pref_sum = [0] * n
suf_sum = [0] * n
for i in range (1, n):
    pref_sum[i] = pref_sum[i-1] + ratings[i-1]
for i in range (n-2,-1,-1):
    suf_sum[i] = ratings[i+1] + suf_sum[i+1]
for i in range (0, n):
    ratings[i] = suf_sum[i] + abs(pref_sum[i] - ratings[i]*i) - ratings[i] * (n-i-1)
    print(ratings[i], end=' ')