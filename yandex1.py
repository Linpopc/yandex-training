def NotMin(L,R, nums):
    min = nums[L]
    for i in range (L+1,R+1):
        if nums[i] < min or nums[i] > min:
            return print(nums[i] if nums[i] > min else min)
    return print('NOT FOUND')


n, m = list(map(int,input().split()))
array = list(map(int,input().split()))
for _ in range (m):
    L, R = list(map(int, input().split()))
    NotMin(L,R,array)