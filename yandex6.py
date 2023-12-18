k = int(input())
n = int(input())
floors = [0] * (n+1)
last_not_null = 0
for i in range (1,n+1):
    floors[i] = int(input())
    if floors[i] != 0:
        last_not_null = i
print(floors)

time_to_park = last_not_null
while last_not_null>0:
    j = last_not_null
