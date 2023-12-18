

def digit_sort(a):
    print('**********')
    d = {}
    for i in a:
        if i[n] in d:
            d[i[n]]
        d[i[n]] = i
    print(d)


n = int(input())
array = []
for _ in range (n):
    digit = str(input())
    array.append(digit)
print("Initial array:")
print(', '.join(array))
n = len(array[0])-1
digit_sort(array)

