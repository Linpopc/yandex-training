a = str(input())
b = str(input())
def IsAnnargam(a,b):
    d = {}
    d1 = {}
    if len(a) != len(b):
        return 'NO'
    for letter in a:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    for letter in b:
        if letter in d1:
            d1[letter] += 1
        else:
            d1[letter] = 1
    return d1==d



res = IsAnnargam(a,b)
print('YES' if res else 'NO')